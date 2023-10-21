import streamlit as st
from textblob import TextBlob
from newspaper import Article
from googletrans import Translator

# Function to summarize the article
def summarize_article(article_url, num_sentences):
    article = Article(article_url)
    article.download()
    article.parse()
    article.nlp()
    summary = article.summary

    blob = TextBlob(summary)
    if num_sentences and num_sentences < len(blob.sentences):
        summary = ' '.join(blob.sentences[:num_sentences])

    return summary

# Function to translate text
def translate_text(text, target_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text

st.title("Article Summarizer and Translator")

# Input for article URL
article_url = st.text_input("Enter the URL of the article to summarize:")

# Input for the number of sentences in the summary
num_sentences = st.number_input("Number of sentences in the summary (0 for full summary):", min_value=0, format="%d")

if st.button("Summarize"):
    if article_url:
        summary = summarize_article(article_url, num_sentences)
        st.subheader("Summary:")
        st.write(summary)
    else:
        st.warning("Please enter the URL of the article to summarize.")

# Language selection for translation
target_language = st.selectbox("Select target language for translation:", ['en', 'es', 'fr', 'de', 'ja', 'ko'])

if st.button("Translate"):
    if 'summary' in locals():
        translated_summary = translate_text(summary, target_language)
        st.subheader("Translated Summary:")
        st.write(translated_summary)
    else:
        st.warning("Please summarize the article before translating.")
