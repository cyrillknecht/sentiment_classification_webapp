from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Load the sentiment analysis pipeline
nlp = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        sentence = request.form['sentence']

        # Classify sentiment
        result = nlp(sentence)[0]
        label = result["label"]
        score = result["score"]

        return render_template('index.html', sentence=sentence, sentiment=label, confidence=score)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=4040)

