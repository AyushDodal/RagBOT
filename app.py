import streamlit as st

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
prompt = st.chat_input("What is up?", accept_file = True, accept_audio = True, file_type = ["jpg", "jpeg", "png"])

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
    # Display file if attached
    if prompt.files:
        for uploaded_file in prompt.files:
            st.markdown(f"**Attachment name:** {uploaded_file.name}")
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
