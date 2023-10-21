from transformers import pipeline
from flask import Flask, request, jsonify

summarizer = pipeline("summarization")

app = Flask(__name__)

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    article = data['article']
    summary = summarizer(article, max_length=150, min_length=50, do_sample=False)
    return jsonify({"summary": summary[0]['summary_text']})

if __name__ == '__main__':
    app.run(debug=True)
