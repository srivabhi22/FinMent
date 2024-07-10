import streamlit as st
import fasttext
import re
import requests

FASTAPI_URL = "http://backend:8000/predict/"  # Replace with your actual FastAPI endpoint

def get_sentiment_from_api(text):
    response = requests.post(FASTAPI_URL, json={"text": text})
    response_data = response.json()
    return response_data["sentiment"], response_data["emoji"]

st.title('Finment: Sentiment Analysis App')

st.write('Enter text below to predict its sentiment:')

user_input = st.text_area('Text input', '')

if user_input:
    sentiment, emoji = get_sentiment_from_api(user_input)
    st.write(f'Sentiment: {sentiment} {emoji}')