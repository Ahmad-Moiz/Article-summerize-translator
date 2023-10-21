import streamlit as st
from transformers import pipeline

# Title and description
st.title("Article Summarizer")
st.write("Enter an article and get a summary.")

# Text input
article = st.text_area("Enter the article here:")

# Check if article is provided
if not article:
    st.warning("Please enter an article to summarize.")
else:
    # Create a modal for the summary
    with st.spinner("Summarizing..."):
        summarizer = pipeline("summarization")
        summary = summarizer(article, max_length=150, min_length=30, do_sample=False)

    # Display the summary
    st.subheader("Summary:")
    st.write(summary[0]["summary"])

# Optional: Add a "Learn more" link
st.write("Learn more at [Hugging Face Transformers](https://huggingface.co/models)")

# (Optional) Footer text
st.markdown(
    """
    ---

    Made with ❤️ by Your Name

    [GitHub Repository](https://github.com/yourusername/your-repo)

    """
)
