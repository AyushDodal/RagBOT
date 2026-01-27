import os
from pypdf import PdfReader

from sentence_splitter import SentenceSplitter
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS


llm = ChatOpenAI(temperature=0.6, model="gpt-4o-mini")


# Generate temporary file path of uploaded docs
def _get_file_path(file_upload):

    temp_dir = "temp"
    os.makedirs(temp_dir, exist_ok=True)  # Ensure the directory exists

    if isinstance(file_upload, str):
        file_path = file_upload  
    else:
        file_path = os.path.join(temp_dir, file_upload.name)
        with open(file_path, "wb") as f:
            f.write(file_upload.getbuffer())
        return file_path


# Load and extract text from one or multiple PDF/docx/pptx/txt files.
def load_documents(file_paths):
    all_text = []

    for file in file_paths:
        reader = PdfReader(file)
        text = "\n".join(page.extract_text() or "" for page in reader.pages)
        all_text.append(text)

    return "\n\n".join(all_text)


def chunkify(text):
    if not isinstance(text, str):
        text = "\n".join(text)
    splitter = SentenceSplitter("en")
    #nodes = splitter.get_nodes_from_documents(text)
    return splitter.split(text)

    
def get_vectorstore(chunks):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(texts=chunks, embedding=embeddings)
    return vectorstore


# Format retrieved documents into a single string
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


# Build and run a Retrieval-Augmented Generation (RAG) chain.
def rag_chain(vectorstore, question):
    qa_chain = (
        {
            "context": vectorstore.as_retriever() | format_docs,
            "question": RunnablePassthrough(),
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return qa_chain.invoke(question)






def main():
    import streamlit as st

    st.title("Echo Bot")
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # React to user input
    prompt = st.chat_input("What is up?", accept_file=True, accept_audio=True, file_type=["pdf", "jpg", "jpeg", "png"])
    if prompt:
        user_prompt = prompt.text
        # Display user message in chat message container
        st.chat_message("user").markdown(user_prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_prompt})

        #if prompt.files:
            #for upload_file in prompt.files:
                #file_paths = [_get_file_path(upload_file) for upload_file in prompt.files]
                #text = load_documents(file_paths)
                #chunks = chunkify(text)
                #vectorstores = get_vectorstore(chunks)
                #assistant_reply = rag_chain(vectorstores, user_prompt)

        
        response = f"Echo: {prompt.text}"
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            
            file_paths = [_get_file_path(upload_file) for upload_file in prompt.files]
            text = load_documents(file_paths)
            chunks = chunkify(text)
            vectorstores = get_vectorstore(chunks)
            assistant_reply = rag_chain(vectorstores, user_prompt)

            
            st.markdown(assistant_reply)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": assistant_reply})






if __name__ == "__main__":
    main()




