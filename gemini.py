import streamlit as st
import google_ai

google_ai.api_key = "AIzaSyDpg8l6j9lchODFkwYzGua2KuNgDcQpiCc"


def generate_article(keyword, language, writing_style, word_count):
    response = google_ai.TextGeneration.create(
        model="gemini-pro",
        prompt=[
            "Write a SEO optimized word article about " + keyword,
            "The article should be " + writing_style,
            "The article length should be " + str(word_count),
            "The article length should be in" + language
        ],
        max_tokens=word_count,
        temperature=0.7
    )
    return response.text


st.title("SEO Article Writer with Gemini AI")

keyword = st.text_input("Enter a keyword:")
language = st.text_input("Enter language:")
writing_style = st.selectbox("Select writing style:", ["Casual", "Informative", "Witty"])
word_count = st.slider("Select word count:", min_value=300, max_value=1000, step=100, value=300)
submit_button = st.button("Generate Article")

if submit_button:
    message = st.empty()
    message.text("Busy generating...")

    try:
        article = generate_article(keyword, language, writing_style, word_count)
        message.text("")
        st.write(article)
        st.download_button(
            label="Download article",
            data=article,
            file_name="Article.txt",
            mime='text/txt',
        )
    except Exception as e:
        st.error("Error occurred: " + str(e))
