import streamlit as st
from textblob import TextBlob

# Streamlit app with enhanced styling
st.set_page_config(
    page_title="Article Summarizer and Translator",
    page_icon="📚",
    layout="centered"
)

# Function to summarize text
def summarize_text(text, num_sentences):
    blob = TextBlob(text)
    summarized_text = blob.sentences[:num_sentences]
    return " ".join(map(str, summarized_text))

# Function to translate text
def translate_text(text, source_lang, target_lang):
    blob = TextBlob(text)
    translated_text = blob.translate(to=target_lang)
    return str(translated_text)

st.title("📝 Article Summarizer and Translator")

# Article input
article = st.text_area("Enter the article text:")

# Summarization
if st.button("Summarize"):
    num_sentences = st.slider("Number of Sentences in Summary", 1, 10, 3)
    if article:
        summarized_text = summarize_text(article, num_sentences)
        st.subheader("Summary:")
        st.write(summarized_text)

# Translation
if st.button("Translate"):
    if article:
        source_lang = st.selectbox("Select source language:", ["auto", "en", "fr", "es", "de", "ja", "ko"])
        target_lang = st.selectbox("Select target language:", ["en", "fr", "es", "de", "ja", "ko"])
        if source_lang != "auto":
            st.write(f"Translating from {source_lang} to {target_lang}...")
            translated_text = translate_text(article, source_lang, target_lang)
            st.subheader("Translated Text:")
            st.write(translated_text)

st.text("")

# Custom styling for the button
st.markdown(
    """
    <style>
    div.stButton > button:first-child {
        background-color: #ff7f50;
        color: white;
        font-family: 'Arial', sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
