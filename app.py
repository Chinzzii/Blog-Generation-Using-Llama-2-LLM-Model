import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers


# Function to get response from Llama 2 model
def getLlamaResponse(input_text, no_words, blog_style):
    llm = CTransformers(
        model="model/llama-2-7b-chat.ggmlv3.q8_0.bin",
        model_type="llama",
        config={"max_new_tokens": 256, "temperature": 0.01},
    )


st.set_page_config(
    page_title="Generate Blogs",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.header("Generate Blogs 🤖")

input_text = st.text_input("Enter the Blog Topic")

col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.text_input("No. of Words")

with col2:
    blog_style = st.selectbox(
        "Writing the Blog for ",
        ("Researchers", "Data Scientist", "Common People"),
        index=0,
    )

submit = st.button("Generate")


# Final Response
if submit:
    st.write(getLlamaResponse(input_text, no_words, blog_style))
