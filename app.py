import streamlit as st
from transformers import pipeline, BartTokenizer, BartForConditionalGeneration
import sumy
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
import requests
import re

# Load the BART model and tokenizer
model_name = "facebook/bart-large-cnn"
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)

# Create a function to summarize text using the BART model
def bart_summarize(text, max_length=150):
    inputs = tokenizer(text, max_length=max_length, return_tensors="pt", truncation=True)
    summary_ids = model.generate(inputs.input_ids, max_length=50, min_length=10, length_penalty=2.0, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

# Create a function to extract sentences from an article using Sumy
def extract_sentences(text, num_sentences=3):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LexRankSummarizer()
    sentences = summarizer(parser.document, num_sentences)
    return [str(sentence) for sentence in sentences]

# Streamlit UI
st.title("Article Summarizer")

# Input for article URL
article_url = st.text_input("Enter the URL of the article you want to summarize:")

if st.button("Summarize"):
    if not article_url:
        st.warning("Please enter a valid article URL.")
    else:
        try:
            # Download the article content from the URL
            response = requests.get(article_url)
            article_text = response.text

            # Extract sentences using Sumy
            extracted_sentences = extract_sentences(article_text)

            # Summarize the extracted sentences using BART
            summary = bart_summarize(" ".join(extracted_sentences))

            # Display the summary
            st.subheader("Summary:")
            st.write(summary)

        except Exception as e:
            st.error("An error occurred. Please check the URL or try again later.")

