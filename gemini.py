import streamlit as st
import google.generativeai as genai

# Set your Gemini API key
api_key = "AIzaSyDpg8l6j9lchODFkwYzGua2KuNgDcQpiCc"

# Configure the Gemini SDK
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-pro")

st.title("Gemini AI Article Generator")

keyword = st.text_input("Enter a keyword")
language = st.text_input("Enter language")
writing_style = st.selectbox("Select writing style:", ["Casual", "Informative", "Witty"])
word_count = st.slider("Select word count:", min_value=300, max_value=1000, step=100, value=300)

if st.button("Generate Article"):
    prompt = f"Write an SEO optimized word article about {keyword} with {writing_style} style in {language} language, in {word_count} words."

    # Call the Gemini API with the prompt, requesting only text
    response = model.generate_content(prompt, max_tokens=word_count, content_types=["text"])

    # Extract the generated text
    article_text = response.text

    # Display the generated text
    st.write(article_text)
