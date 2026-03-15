# CinemaPulse - Movie Recommendation Web App

## Introduction
CinemaPulse is a movie recommendation web application built using Streamlit. The app suggests movies similar to a selected movie using a content-based recommendation system.

The recommendation engine analyzes movie metadata such as genres, keywords, cast, and overview to find similar movies. It uses Natural Language Processing techniques and cosine similarity to recommend movies with similar content.

The application is deployed on Streamlit Cloud and provides an interactive interface where users can select a movie and instantly get recommendations.

---

## Live Application

Streamlit App: https://your-streamlit-link

---

## Features

- Interactive movie recommendation interface
- Content-based recommendation system
- Instant movie suggestions
- Simple and user-friendly UI
- Deployed on Streamlit Cloud

---

## How the Recommendation System Works

1. Movie metadata such as genres, keywords, cast, and overview are combined.
2. Text preprocessing is applied including:
   - Lowercase conversion
   - Tokenization
   - Stemming using PorterStemmer
3. The processed text is converted into numerical format using CountVectorizer (Bag of Words).
4. Cosine similarity is calculated between movie vectors.
5. Movies with the highest similarity scores are recommended.

---

## Technologies Used

Python  
Streamlit  
NumPy  
Pandas  
NLTK  
PorterStemmer  
Scikit-learn  
CountVectorizer  
Cosine Similarity  

---

## Project Structure

CinemaPulse/

app.py  
movies.pkl  
similarity.pkl  
requirements.txt  
README.md  

---

## Running the App Locally

Clone the repository

Install dependencies

Run the Streamlit application

The app will open automatically in your browser.

---

## Deployment

The application is deployed using Streamlit Cloud. The deployment process includes:

1. Uploading the project to GitHub
2. Connecting the repository to Streamlit Cloud
3. Deploying the app directly from the GitHub repository

---

## Conclusion

CinemaPulse demonstrates how a machine learning recommendation system can be transformed into an interactive web application. By combining NLP techniques with similarity-based recommendations, the app provides users with quick and relevant movie suggestions.