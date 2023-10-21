import streamlit as st
import nltk
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Function to read and preprocess the article
def read_article(article):
    sentences = nltk.sent_tokenize(article)
    sentences = [sentence for sentence in sentences if len(sentence) > 10]  # Filter out very short sentences
    return sentences

# Function to compute sentence similarity based on cosine similarity
def sentence_similarity(sent1, sent2, stopwords):
    words1 = nltk.word_tokenize(sent1)
    words2 = nltk.word_tokenize(sent2)

    words1 = [word.lower() for word in words1 if word.isalnum()]
    words2 = [word.lower() for word in words2 if word.isalnum()]

    all_words = list(set(words1 + words2)

    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)

    for word in words1:
        if word in stopwords:
            continue
        vector1[all_words.index(word)] += 1

    for word in words2:
        if word in stopwords:
            continue
        vector2[all_words.index(word)] += 1

    return 1 - cosine_distance(vector1, vector2)

# Function to create a similarity matrix of sentences
def build_similarity_matrix(sentences, stopwords):
    similarity_matrix = np.zeros((len(sentences), len(sentences))

    for i in range(len(sentences)):
        for j in range(len(sentences)):
            if i == j:  # Skip comparing a sentence to itself
                continue
            similarity_matrix[i][j] = sentence_similarity(sentences[i], sentences[j], stopwords)

    return similarity_matrix

# Function to generate the article summary
def generate_summary(article, top_n=5):
    sentences = read_article(article)
    stop_words = set(stopwords.words('english'))
    sentence_similarity_matrix = build_similarity_matrix(sentences, stop_words)

    # Create a graph from the similarity matrix
    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_matrix)

    # Use the PageRank algorithm to rank the sentences
    scores = nx.pagerank(sentence_similarity_graph)

    # Sort the sentences by score
    ranked_sentences = sorted(((scores[i], sentence) for i, sentence in enumerate(sentences)), reverse=True)

    # Get the top N sentences as the summary
    summary = " ".join([sentence for _, sentence in ranked_sentences[:top_n]])
    return summary

# Streamlit web app
st.title("Article Summarizer")
user_article = st.text_area("Enter your article here:")

if st.button("Summarize"):
    if user_article:
        summary = generate_summary(user_article)
        st.subheader("Summary:")
        st.write(summary)
    else:
        st.warning("Please enter an article to summarize.")
