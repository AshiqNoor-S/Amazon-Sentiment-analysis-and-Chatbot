import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# matplotlib inline
import time
from datetime import datetime
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
from scrapingbee import ScrapingBeeClient
import openai
import streamlit as st

openai.api_key = "xxx" #Enter your api key here

def generate_chatbot_response(prompt):

    response = openai.Completion.create(
        engine="text-davinci-003",  
        prompt=prompt,
        max_tokens=150, 
        temperature=0.7  
    )
    return response['choices'][0]['text'].strip()

def main():
    print("Welcome to the Product Inquiry Chatbot!")
    print("Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break

        prompt = f"You: {user_input}\nChatbot:"
        chatbot_response = generate_chatbot_response(prompt)

        print(f"Chatbot: {chatbot_response}")

if __name__ == "__main__":
    main()