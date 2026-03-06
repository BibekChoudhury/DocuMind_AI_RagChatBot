import os
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import ChatPromptTemplate

# Define path for vector store
VECTOR_PATH = "vectors"

# Load environment variables
load_dotenv()
HF_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

def qa_brain(query):
    # 1. Load embedding model
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # 2. Load saved FAISS vector store
    vector_store = FAISS.load_local(
        VECTOR_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    # 3. Create retriever and get docs
    retriever = vector_store.as_retriever(search_kwargs={"k": 4})
    docs = retriever.invoke(query)
    context = "\n\n".join([doc.page_content for doc in docs])

    # 4. FIX: Use ChatHuggingFace wrapper
    # This ensures the 'conversational' task is used correctly
    llm_base = HuggingFaceEndpoint(
        repo_id="Qwen/Qwen2.5-72B-Instruct",
        huggingfacehub_api_token=HF_TOKEN,
        temperature=0.2,
        max_new_tokens=512,
        # Force the Hugging Face serverless provider to avoid Together AI errors
        extra_body={"provider": "hf-inference"} 
    )
    
    # WRAP the LLM to handle chat templates
    llm = ChatHuggingFace(llm=llm_base)

    # 5. FIX: Use a ChatPromptTemplate for better structure
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "You are an AI assistant. Answer strictly using the provided context. If the answer isn't there, say: 'The answer is not available in the document.'"),
        ("user", "Context:\n{context}\n\nQuestion: {question}")
    ])

    # 6. Generate Response
    # Format the prompt with variables and invoke
    chain = prompt_template | llm
    response = chain.invoke({"context": context, "question": query})

    return response.content # .content gives you the actual text string