import streamlit as st
import streamlit.components.v1 as components
import google.generativeai as genai

# Set your Gemini API key
api_key = "AIzaSyDpg8l6j9lchODFkwYzGua2KuNgDcQpiCc"

# Configure the Gemini SDK
genai.configure(api_key=api_key)
generation_config = {"temperature":0.9,"top_p":1,"top_k":1,"max_output_tokens":2048}
model = genai.GenerativeModel("gemini-pro",generation_config=generation_config)

st.title("Gemini AI Article Generator")
keyword = st.text_input("Enter a keyword")
language = st.text_input("Enter language")
writing_style = st.selectbox("Select writing style:", ["Casual", "Informative", "Witty"])
word_count = st.slider("Select word count:", min_value=300, max_value=1000, step=100, value=300)
components.html("""
<script type='text/javascript' src='//demiseskill.com/ba/36/28/ba36280aacfbc4c6c4b68d106c59564d.js'></script>""")

if st.button("Generate Article"):
    prompt = f"Generate an SEO-optimized article about {keyword} in {language}. The article should be approximately {word_count} words long and structured with clear headings, subheadings, and paragraphs. Use relevant keywords throughout the text and create engaging content that effectively addresses the topic."

    # Call the Gemini API with the prompt, requesting only text
    response = model.generate_content(prompt)

    # Extract the generated text
    article_text = response.text

    # Display the generated text
    st.write(article_text)
