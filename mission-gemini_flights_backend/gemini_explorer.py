import vertexai
import streamlit as st
from vertexai.preview import generative_models
from vertexai.preview.generative_models import GenerativeModel, Part, Content, ChatSession


project = "plated-mantra-432301-b9"
vertexai.init(project = project)

config = generative_models. GenerationConfig(
    temperature=0.4
)

# Load model with config
model = GenerativeModel(
    "gemini-pro",
    generation_config = config
)

chat = model.start_chat()


# helper function to display and send streamlit messages
def llm_function(chat: ChatSession, query):
    response = chat.send_message(query)
    output = response.candidates[0].content.parts[0].text
    
    st.write("Model:", output)

    st.session_state.messages.append(
    {
    "role": "user",
    "content": query
    })

    st.session_state.messages.append(
    {
    "role": "model",
    "content": output})

    return response


st.title("Gemini Explorer")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [ ]

for message in st.session_state.messages:
    content = Content (
        role = message["role"],
        parts = [Part.from_text(message["content"])])

    try:
        if message["role"] == "user":
            st.write("User:", message["content"])
        elif message["role"] == "model":
            st.write("Model:", message["content"])

    except Exception as e:
        print(e)
        print(message)

    chat.history.append(content)

if len(st.session_state.messages) == 0:
    # initial_prompt = "Introduce yourself as ReX, an assistant powered by Google Gemini. You use emojis to be interactive"
    name = st.text_input("Enter your name:")
    print(name)

    if name:
        initial_prompt = "Arrr matey! Introduce yourself as ReX, a savvy assistant powered by Google Gemini. Ye use emojis to be interactive. Also use this name to address user - "+ name
        llm_function(chat, initial_prompt)

query = st.text_input("Gemini Explorer")

if query:
    st.write("User:", query)

    response = llm_function(chat, query)