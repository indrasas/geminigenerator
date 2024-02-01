import streamlit as st
from google.api_core.client_options import ClientOptions
from google.cloud import language_v1

# Set your Gemini API key
api_key = "AIzaSyDpg8l6j9lchODFkwYzGua2KuNgDcQpiCc"

# Create a client using the API key
client_options = ClientOptions(api_key=api_key)
client = language_v1.LanguageServiceClient(client_options=client_options)

st.title("Gemini AI Article Generator")

keyword = st.text_input("Enter a keyword")
language = st.text_input("Enter language")
writing_style = st.selectbox("Select writing style:", ["Casual", "Informative", "Witty"])
word_count = st.slider("Select word count:", min_value=300, max_value=1000, step=100, value=300)

if st.button("Generate Article"):
    prompt = f"Write an SEO optimized word article about {keyword} with {writing_style} style in {language} language, in {word_count} words."

    # Call the Gemini API with the prompt
    document = language_v1.Document(
        content=prompt,
        type_=language_v1.Document.Type.PLAIN_TEXT
    )
    response = client.annotate_text(request={'document': document})

    # Retrieve and display the generated text
    article = response.text.annotations[0].text.content
    st.write(article)
