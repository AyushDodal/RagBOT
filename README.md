# RagBOT

A simple Retrieval-Augmented Generation (RAG) chatbot built with LangChain, OpenAI, FAISS, and Streamlit.
Upload documents and ask questions grounded in your data.
LINK : https://ragbot-y3srqbqyet7bqzz5yt9dui.streamlit.app/


## How it Works

1. Upload a document

2. Text is extracted and split into chunks

3. Chunks are embedded and stored in FAISS

4. Relevant chunks are retrieved per query

5. LLM answers using retrieved context

## Features
PDF text ingestion

Sentence-based chunking

Vector search with FAISS

Context-aware answers using OpenAI (gpt-5.1)

Deployed on Streamlit Cloud

Optional password protection


## Architecture Diagram:

![unnamed](https://github.com/user-attachments/assets/b1677b41-2f4f-4536-8fb9-0cb6a978f29c)



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
