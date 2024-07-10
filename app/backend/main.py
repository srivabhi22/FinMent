from fastapi import FastAPI
from pydantic import BaseModel
import fasttext
import re

app = FastAPI()

model_path="C:/Users/HP/OneDrive - IIT Kanpur/Desktop/FinMent/app/model/fasttext.bin"
model = fasttext.load_model(model_path)  # Replace with your model loading code

class InputData(BaseModel):
    text: str

def predict_sentiment(model, text):
    print(text)
    sentence = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    sentence = sentence.lower()
    print(f"The statement is: {sentence}")
    prediction = model.predict(sentence)
    length = len("__label__")

    sentiment = prediction[0][0]
    sentiment = sentiment[length:]
    return sentiment

@app.post("/predict/")
def predict_sentiment_api(input_data: InputData):
    text = input_data.text
    sentiment = predict_sentiment(model, text)
    if sentiment == 'positive':
        emoji = '😊'
    elif sentiment == 'neutral':
        emoji = '😐'
    else:
        emoji = '😞'
    return {"sentiment": sentiment, "emoji": emoji}
