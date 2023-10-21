import streamlit as st
from transformers import pipeline

# Create a function to summarize text using the transformers library
def summarize_text(text):
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=150, min_length=30, do_sample=False)
    return summary[0]["summary"]

# Streamlit app with enhanced styling
st.set_page_config(
    page_title="Article Summarizer",
    page_icon="📄",
    layout="centered"
)

st.title("📖 Article Summarizer")

# Create a button to open the summarization modal
if st.button("Summarize Article"):
    # Create a text area for user to input the article
    with st.form("article_form"):
        st.write("Paste the article you want to summarize below:")
        article_text = st.text_area("")

        # Create a button to submit the form
        submit_button = st.form_submit_button("Summarize")

    # Check if the form was submitted
    if submit_button:
        if article_text:
            # Call the summarization function
            summary = summarize_text(article_text)
            st.subheader("Summary:")
            st.write(summary)
        else:
            st.warning("Please enter an article to summarize.")
