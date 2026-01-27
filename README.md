# RagBOT

A simple Retrieval-Augmented Generation (RAG) chatbot built with LangChain, OpenAI, FAISS, and Streamlit.
Upload documents and ask questions grounded in your data.

## Features
PDF text ingestion

Sentence-based chunking

Vector search with FAISS

Context-aware answers using OpenAI (gpt-5.1)

Deployed on Streamlit Cloud

Optional password protection


## Architecture Diagram:
<img width="836" height="378" alt="Architectural Diagram" src="https://github.com/user-attachments/assets/397ff50b-f49f-47cf-84a0-8af8fd30e35e" />



## Tech Stack
Python

Streamlit

LangChain

OpenAI API

FAISS

PyPDF

sentence-splitter



## SETUP
1. Fork / clone the repo

2. Add secrets in Streamlit → App → Settings → Secrets:
OPENAI_API_KEY="sk-xxxx"
APP_PASSWORD="yourpassword"

3. Deploy!🚀
