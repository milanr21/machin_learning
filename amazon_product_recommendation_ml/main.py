import numpy as np
import pandas as pd
import nltk
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st
from  PIL import Image


# Load the dataset from

data = pd.read_csv("amazon_product.csv")

#Removing uncessaart columns

data = data.drop('id', axis=1);

# Tokenization defination
stemmer = SnowballStemmer("english")
def tokenize_stem(text):
    tokens = nltk.word_tokenize(text.lower())
    stemmed = [stemmer.stem(w) for w in tokens]
    return " ".join(stemmed)


# steam token column
data['stemmed_tokens'] = data.apply(lambda row: tokenize_stem(row["Title"] + " " + row["Description"]), axis=1)

# Create a TfidfVectorizer with the tokenize_stem function
tfidf_vectorizer = TfidfVectorizer(tokenizer=tokenize_stem)

def cosine_sim(txt1, txt2):
    # Use fit_transform to create the TF-IDF matrix
    tx1_concatenated = " ".join(txt1)
    tx2_concatenated = " ".join(txt2)
    matrix = tfidf_vectorizer.fit_transform([ tx1_concatenated, tx2_concatenated])
    
    # Calculate cosine similarity
    similarity_matrix = cosine_similarity(matrix)
    
    # Return the cosine similarity value for the two texts
    return similarity_matrix[0, 1]

# Create a function to get the most similar products
def recommend_product(query, df):
    # Tokenize and stem the input query
    tokenized_query = tokenize_stem(query)

    # Calculate cosine similarity between the query and each product in the dataset
    df['similarity'] = df['stemmed_tokens'].apply(lambda x: cosine_sim(tokenized_query, x))

    # Sort the DataFrame based on similarity in descending order and take the top 10 results
    final_df = df.sort_values(by=['similarity'], ascending=False).head(10)

    # Select specific columns ('Title', 'Description', 'Category') for the final recommendation
    final_df = final_df[['Title', 'Description', 'Category']]

    # Return the DataFrame with the top 10 recommended products
    return final_df


#web app 
img = Image.open("amazon_img.png")
st.image(img, width = 500)
st.title("Amazon Product Recommender")

wuery = st.text_input("Enter the product you are looking for")

submit = st.button("Recommend")

if submit:
    recommendations = recommend_product(wuery, data)
    st.table(recommendations)
    st.balloons()