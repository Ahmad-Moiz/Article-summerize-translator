import streamlit as st
from transformers import BartForConditionalGeneration, BartTokenizer

# Load the BART pre-trained model and tokenizer
model_name = "facebook/bart-large-cnn"
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)

# Define the summarization function
def summarize_article(article):
    # Tokenize and encode the article
    inputs = tokenizer.encode("summarize: " + article, return_tensors="pt", max_length=1024, truncation=True)

    # Generate the summary
    summary_ids = model.generate(inputs, max_length=150, min_length=50, length_penalty=2.0, num_beams=4, early_stopping=True)

    # Decode and return the summary
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

# Streamlit UI
st.title("Article Summarizer")

# Input box for the article
article = st.text_area("Enter the article")

if st.button("Summarize"):
    summary = summarize_article(article)
    st.subheader("Summary:")
    st.write(summary)
