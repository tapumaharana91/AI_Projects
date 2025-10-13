import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_community.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader

from dotenv import load_dotenv
load_dotenv()

groq_api_key=os.getenv("GROQ_API_KEY")

st.title("ChatGroq demo with embeddings")

llm=ChatGroq(groq_api_key=groq_api_key,
             model='llama-3.3-70b-versatile')

prompt=ChatPromptTemplate.from_template(
    """
Answer the following question based only on the context provided.
Think step by step before providing a detailed answer.
I will tip you $1000 if the user finds the answer helpful.
<context>
{context}
</context>
Question: {input}
"""
)

def vector_embedding():

    if "vectors" not in st.session_state:
        st.session_state.embeddings=OllamaEmbeddings(model='nomic-embed-text')
        st.session_state.loader=PyPDFDirectoryLoader("C:/Users/ASUS/Downloads/Langchain/groq")
        st.session_state.docs=st.session_state.loader.load()
        st.session_state.text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
        st.session_state.final_documents=st.session_state.text_splitter.split_documents(st.session_state.docs[:20])
        st.session_state.vectors=FAISS.from_documents(st.session_state.final_documents,st.session_state.embeddings)

prompt1=st.text_input("Enter your Questions from the Documents")


if st.button("Documents Embeddings"):
    vector_embedding()
    st.write("Vectorstore DB is ready")

import time



if prompt1:
    document_chain=create_stuff_documents_chain(llm,prompt)
    retriever=st.session_state.vectors.as_retriever()
    retrieval_chain=create_retrieval_chain(retriever,document_chain)
    start=time.process_time()
    response=retrieval_chain.invoke({'input':prompt1})
    print("Response time: ",time.process_time()-start)
    st.write(response['answer'])

    # with a streamlit expander

    with st.expander("Document Similarity Search"):
        # Find relavant chunks
        for i,doc in enumerate(response['context']):
            st.write(doc.page_content)
            st.write("-------------------------")

