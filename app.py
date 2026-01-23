import streamlit as st
from llama_index.core import SimpleDirectoryReader
from llama_index.readers.file import PDFReader
from llama_index.core.node_parser import SentenceSplitter


def chunkify_from_upload(uploaded_file):
    # 1. Extract TEXT from the binary file
    reader = PDFReader()
    # The reader handles the bytes for you
    documents = reader.load_data(file=uploaded_file) 
    
    # 2. Chunk the extracted TEXT
    splitter = SentenceSplitter(chunk_size=1024)
    nodes = splitter.get_nodes_from_documents(documents)
    
    return nodes


#def vector_store():

















def main():
  st.set_page_config(
    page_title = "RAG-BOT",
    page_icon = "📚 🔎 🤖 💬"
  )
  
  st.write("Hello!👋 This is a Retrieval Augmented Generation Bot - RAG-BOT. You can upload files, they will get stored in a Vector Database for the LLM to refer." )
  
  
  
  # Initialize chat history
  if "messages" not in st.session_state:
      st.session_state.messages = []
  
  # Display chat messages from history on app rerun
  for message in st.session_state.messages:
      with st.chat_message(message["role"]):
          st.markdown(message["content"])
  
  # React to user input
  prompt = st.chat_input("What is up?", accept_file = True, accept_audio = True, file_type = ["pdf", "jpg", "jpeg", "png"])
  
  if prompt:
      # Display user message in chat message container
      if prompt.text:
          st.chat_message("user").markdown(f"**Your message:** {prompt.text}")
          # Add user message to chat history
          st.session_state.messages.append({"role": "user", "content": prompt})
  
      
      
      response = f"Echo: {prompt.text}"
      # Display assistant response in chat message container
      with st.chat_message("assistant"):
          st.markdown(response)
      # Display file name if attached
      if prompt.files:
          for uploaded_file in prompt.files:
              st.markdown(f"**Attachment name:** {uploaded_file.name}")
              chunkify_from_upload(uploaded_file)
              #st.markdown(f"**File: ** {nodes}")
      # Add assistant response to chat history
      st.session_state.messages.append({"role": "assistant", "content": response})





if __name__=="__main__":
  main()
