import streamlit as st
import os
from ingest import process_data
from qa import qa_brain

# Folder for uploaded files
DATA_PATH = "data"

# 1. App setup (Tab title and icon)
st.set_page_config(
    page_title="DocuMind | NotebookLM",
    page_icon="🧬",  
    layout="wide"
)

# 2. Initialize memory for chat and file list
if "messages" not in st.session_state:
    st.session_state.messages = [] 

if "processed_files" not in st.session_state:
    st.session_state.processed_files = [] 

# 3. Sidebar for uploading PDFs
with st.sidebar:
    st.title("📚 Sources")
    uploaded_files = st.file_uploader("Upload PDFs", type="pdf", accept_multiple_files=True)
    
    if uploaded_files:
        for uploaded_file in uploaded_files:
            # Only index if the file is new
            if uploaded_file.name not in st.session_state.processed_files:
                if not os.path.exists(DATA_PATH):
                    os.makedirs(DATA_PATH)
                
                # Save file to local folder
                file_path = os.path.join(DATA_PATH, uploaded_file.name)
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.read())
                
                # Process PDF into the RAG system
                with st.spinner(f"Indexing {uploaded_file.name}..."):
                    process_data(file_path)
                    st.session_state.processed_files.append(uploaded_file.name)
                st.toast(f"{uploaded_file.name} ready!", icon="✅")

    # Reset chat button
    if st.button("Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# 4. Main UI title
st.title("📄 DocuMind AI")

# Display previous chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. Chat input and response logic
if query := st.chat_input("Ask something about your documents..."):
    # Store user question
    st.session_state.messages.append({"role": "user", "content": query})
    
    with st.chat_message("user"):
        st.markdown(query)

    # Generate answer from AI
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                answer = qa_brain(query)
                st.markdown(answer)
                # Store AI answer
                st.session_state.messages.append({"role": "assistant", "content": answer})
            except Exception as e:
                st.error(f"Error: {str(e)}")