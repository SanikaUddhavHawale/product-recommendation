# Import libraries
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import streamlit as st

# Load dataset
@st.cache_data
def load_data():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx"
    df = pd.read_excel(url, engine="openpyxl")  # Explicitly specify the engine
    return df

# Preprocess dataset
def preprocess_data(df):
    # Remove rows with missing CustomerID
    df = df.dropna(subset=['CustomerID'])
    
    # Convert CustomerID to int
    df['CustomerID'] = df['CustomerID'].astype(int)
    
    # Aggregate product descriptions for each user
    user_products = df.groupby('CustomerID')['Description'].apply(lambda x: ' '.join(x)).reset_index()
    return user_products

# Build the recommendation system
def build_model(user_products):
    # Transform product descriptions into TF-IDF feature vectors
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(user_products['Description'])
    
    # Compute cosine similarity
    similarity_matrix = cosine_similarity(tfidf_matrix)
    return similarity_matrix

# Recommend products for a user
def recommend_products(user_id, user_products, similarity_matrix):
    # Find index of the user
    user_idx = user_products[user_products['CustomerID'] == user_id].index
    
    if len(user_idx) == 0:
        return ["User ID not found. Please try another."]
    
    # Get similarity scores for the user
    user_similarity = similarity_matrix[user_idx[0]]
    
    # Get the indices of the top similar users
    similar_users = user_similarity.argsort()[::-1][1:11]  
    
    # Gather product recommendations
    recommended_products = []
    for idx in similar_users:
        recommended_products.extend(user_products.iloc[idx]['Description'].split(' '))
    
    # Return the top 10 recommended products
    return list(set(recommended_products))[:10]

# Streamlit Dashboard
def main():
    st.title("Product Recommendation Dashboard")
    
    # Load dataset
    df = load_data()
    
    # Display raw dataset
    st.subheader("Dataset Preview")
    st.dataframe(df.head())
    
    # Preprocess dataset
    st.text("Preprocessing data...")
    user_products = preprocess_data(df)
    st.text("Data preprocessing completed!")
    
    # Build the recommendation model
    st.text("Building recommendation model...")
    similarity_matrix = build_model(user_products)
    st.text("Model built successfully!")
    
    # User input for Customer ID
    user_id = st.text_input("Enter your Customer ID", "")
    
    if st.button("Get Recommendations"):
        if user_id:
            try:
                user_id = int(user_id)  # Convert input to integer
                recommendations = recommend_products(user_id, user_products, similarity_matrix)
                st.subheader("Recommended Products")
                st.write(recommendations)
            except ValueError:
                st.error("Please enter a valid numeric Customer ID.")
        else:
            st.error("Please enter a Customer ID.")

if __name__ == "__main__":
    main()
