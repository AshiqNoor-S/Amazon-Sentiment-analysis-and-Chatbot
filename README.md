# Amazon-Sentiment-analysis-and-Chatbot

## Overview
The project involves the deployment of a versatile web application that seamlessly combines sentiment analysis of Amazon product reviews and an interactive chatbot for customer inquiries. This integration is achieved through two distinct scripts: app.py and chatbot.py.

The app.py script utilizes the Streamlit framework to create a user-friendly interface that guides users through two core functionalities. Firstly, the "Sentiment Analysis" page prompts users to input an Amazon product URL. Upon clicking the "Scrape Reviews and Perform Sentiment Analysis" button, the script scrapes relevant details from the product page using the ScrapingBeeClient library and analyzes the sentiment of extracted product reviews with the help of the TextBlob sentiment analysis library. Secondly, the "Chatbot" page empowers users to engage with an AI-powered chatbot. After submitting a question or inquiry, the chatbot generates responses using the OpenAI API, offering real-time interactions.

In parallel, the chatbot.py script concentrates on the chatbot's standalone functionality. It leverages the OpenAI API to generate responses based on user input prompts, forming a dynamic and responsive conversation experience. This script is designed for console-based interactions and showcases the chatbot's capabilities in a conversational context.

## Project Structure
**app1.py**: Main Streamlit application file combining sentiment analysis and chatbot functionality.
**chatbot.py**: Implementation of the chatbot's functionality.
**requirements.txt**: List of Python dependencies needed to run the application.

## Getting Started
1. **Clone the Repository**: Clone this repository to your local machine 
2. **Install Dependencies**: Navigate to the project folder and install dependencies:
   cd amazon-sentiment-chatbot
   pip install -r requirements.txt
4. **Configure Chatbot Responses**: Customize chatbot responses in `chatbot.py` for various customer inquiries and add the api keys.
5. **Run the Application**: Launch the Streamlit application:


