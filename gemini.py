import streamlit as st
import streamlit.components.v1 as components
import google.generativeai as genai
import random
import time
import webbrowser

# Array of API keys
api_keys = [
    "AIzaSyDpg8l6j9lchODFkwYzGua2KuNgDcQpiCc",
    "AIzaSyCR3Bi5DiMdkZaO-HpX2Jqq51_HKwfxif4",
    "AIzaSyDy0O2i6kbNszNoR-pxxCMil6DHHnxlUeM",
    "AIzaSyA07lPucysQRJVl8iW4BvKy9bIoBbZif_o",
    "AIzaSyAMySu6L8IFFRYxy_Mw3P8saC1tim9SeBk",
    "AIzaSyAeIGjl19HgjjyP4oYcfmMIBi2DJQj3hFY",
    "AIzaSyB4DC9PAHumJH1G8-Xhn4zkia6jmCSQT9w",
    # Add more API keys as needed
]

# Randomly select an API key
api_key = random.choice(api_keys)

# Configure the Gemini SDK
genai.configure(api_key=api_key)
generation_config = {"temperature": 0.9, "top_p": 1, "top_k": 1, "max_output_tokens": 2048}
model = genai.GenerativeModel("gemini-pro", generation_config=generation_config)
st.set_page_config(
   page_title="Article Generator",
   page_icon="🧊",
)
st.title("Article Generator")
keyword = st.text_input("Enter a keyword")
language = st.text_input("Enter language")
st.caption('Insert language for the result. ex : Indonesia, English, Japanese, French, Korean, Germany, Chinese Simplified')
writing_style = st.selectbox("Select writing style:", ["Casual", "Informative", "Witty"])
word_count = st.slider("Select word count:", min_value=300, max_value=1000, step=100, value=300)

if st.button("Generate Article"):
        prompt = f"Generate an SEO-optimized article about {keyword} in {language}. The article should be approximately {word_count} words long and structured with clear headings, subheadings, and paragraphs. Use relevant keywords throughout the text and create engaging content that effectively addresses the topic. Add 5 FAQ related to {keyword} in the end."
        # Call the Gemini API with the prompt, requesting only text
        response = model.generate_content(prompt)
        # Extract the generated text
        article_text = response.text
        # Display the generated text
        st.write(article_text)

components.html("""
<script type="text/javascript" src="//demiseskill.com/bf/48/25/bf48250f632348ae4ae0dd43a3a7b1b8.js"></script>""")

