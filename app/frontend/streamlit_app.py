import streamlit as st
import fasttext
import re

model=fasttext.load_model("fasttext.bin")  # Replace with your model loading code

def predict_sentiment(model,text):
    print(text)
    sentence = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    sentence = sentence.lower()
    print(f"The statement is: {sentence}")
    prediction = model.predict(sentence)
    length=len("__label__")

    sentiment=prediction[0][0]
    sentiment=sentiment[length:]
    return sentiment

def get_sentiment(text):
    prediction = predict_sentiment(model, text)  
    if prediction == 'positive':
        emoji = '😊'
        sentiment = 'Positive'
    elif prediction == 'neutral':
        emoji = '😐'
        sentiment = 'Neutral'
    else:
        emoji = '😞'
        sentiment = 'Negative'
    return emoji, sentiment


st.title('Finment: Sentiment Analysis App')

st.write('Enter text below to predict its sentiment:')

user_input = st.text_area('Text input', '')

if user_input:
    emoji, sentiment = get_sentiment(user_input)
    st.write(f'Sentiment: {sentiment} {emoji}')
