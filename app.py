from flask import Flask, request, jsonify,render_template
import numpy as np
import fasttext
import re

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["GET","POST"])
def predict():
    text = request.form['text']
    print(text)
    sentence = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    sentence = sentence.lower()
    print(f"The statement is: {sentence}")
    
    model=fasttext.load_model("fasttext.bin")
    prediction = model.predict(sentence)
    length=len("__label__")

    sentiment=prediction[0][0]
    sentiment=sentiment[length:]
    
    if sentiment == 'positive':
        predicted_sentiment = 'Positive'
        color = 'green'  # Use CSS classes for visual feedback
    elif sentiment == 'negative':
        predicted_sentiment = 'Negative'
        color = 'red'
    else:
        predicted_sentiment = 'Neutral'
        color = 'gray'
    return render_template('index.html', text=text, predicted_sentiment=predicted_sentiment, color=color)
        

if __name__ == "__main__":
    app.run(debug=True)


