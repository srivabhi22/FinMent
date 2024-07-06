from flask import Flask, request, jsonify,render_template
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

app = Flask(__name__)

# Load trained model
model = LogisticRegression()
# model.load("sentiment_model.pkl")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    statement = request.json["statement"]
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform([statement])
    y_pred = model.predict(X)
    sentiment = "Positive" if y_pred[0] == 1 else "Negative"
    return jsonify({"sentiment": sentiment})

if __name__ == "__main__":
    app.run(debug=True)