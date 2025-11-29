import streamlit as st
import os
from pdf_utils import extract_text_from_pdf
from indexer import index_documents
from retriever import retrieve_relevant_docs
from generator_hf import generate_answer
from utils import clean_text, split_text_into_chunks

st.title("StudyMate - AI-Powered Academic Assistant")

st.sidebar.header("Upload Documents")
uploaded_files = st.sidebar.file_uploader("Upload PDF files", type="pdf", accept_multiple_files=True)

if uploaded_files:
    documents = []
    for uploaded_file in uploaded_files:
        text = extract_text_from_pdf(uploaded_file)
        text = clean_text(text)
        chunks = split_text_into_chunks(text)
        documents.extend(chunks)
    
    # Index the documents
    index = index_documents(documents)
    st.sidebar.success("Documents indexed successfully!")
    
    # Question input
    question = st.text_input("Ask a question about your documents:")
    
    if question:
        # Retrieve relevant documents
        relevant_docs = retrieve_relevant_docs(question, index, documents)
        
        # Generate answer
        context = " ".join(relevant_docs)
        answer = generate_answer(question, context)
        
        st.subheader("Answer:")
        st.write(answer)
        
        st.subheader("Relevant Sections:")
        for i, doc in enumerate(relevant_docs[:3]):  # Show top 3
            st.write(f"**Section {i+1}:** {doc[:500]}...")
else:
    st.write("Please upload PDF documents to get started.")
