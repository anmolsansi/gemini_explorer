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
prompt = "generate a description of a peaceful landscape in 20 words"
response = model.generate_content(prompt)

# response = chat.ask(prompt)
st.write(response)
st.code("streamlit run gemini_explorer.py")