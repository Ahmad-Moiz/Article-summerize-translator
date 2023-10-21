import spacy
import streamlit as st

def article_summarizer(article_text, num_sentences=3):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(article_text)
    sentence_importance = {}
    for sentence in doc.sents:
        sentence_tokens = [token for token in sentence if not token.is_stop]
        sentence_rank = sum(token.rank for token in sentence_tokens)
        sentence_importance[sentence] = sentence_rank
    sorted_sentences = sorted(sentence_importance, key=lambda x: sentence_importance[x], reverse=True)
    summary = " ".join(str(sentence) for sentence in sorted_sentences[:num_sentences])
    return summary

st.title("Article Summarizer")

article = st.text_area("Enter your article here:")
num_sentences = st.slider("Select the number of sentences for the summary:", 1, 10, 3)

if st.button("Summarize"):
    if article:
        summary = article_summarizer(article, num_sentences)
        st.subheader("Summary:")
        st.write(summary)
    else:
        st.warning("Please enter an article to summarize.")
