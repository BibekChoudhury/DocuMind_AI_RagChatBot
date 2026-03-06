from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import os

# Define paths for data and vector store
 
DATA_PATH = "data"
VECTOR_PATH = "vectors"

#Process the data and create vector store

def process_data(file_path):
    
    loader = PyPDFLoader(file_path)
    data = loader.load()
    
# Split the data into chunks
    
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
# Create embeddings and vector store
    
    chunks = splitter.split_documents(data)
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
# Create vector store and save it locally
    
    vector_store = FAISS.from_documents(chunks, embeddings)
    vector_store.save_local(VECTOR_PATH)
    
    return vector_store    