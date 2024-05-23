import streamlit as st
from fetch_news import fetch_news
from generate_commentary import generate_commentary
from datetime import datetime

st.title("SocialAye")

# Define the categories
categories = ['technology', 'entertainment', 'sports', 'science']

# Select a category
category = st.sidebar.selectbox('Choose a category', categories)

# Fetch news articles
articles = fetch_news(category)

if articles:
    # Display articles
    st.title(f"Today's Top {category.capitalize()} News by MacAI")
    
    for article in articles[:3]:  # Display top 3 articles for simplicity
        st.subheader(article.get('title', 'No title'))
        st.write(article.get('description', 'No description available'))
        commentary = generate_commentary(article.get('title', 'No title'), article.get('description', 'No description available'))
        st.markdown(f"**MacAI Commentary:**\n\n{commentary}")
        published_at = article.get('publishedAt', article.get('published', 'Unknown date'))
        try:
            published_at = datetime.strptime(published_at, '%Y-%m-%dT%H:%M:%SZ').strftime('%B %d, %Y %H:%M')
        except ValueError:
            pass
        st.markdown(f"Published at: {published_at}")

st.write("Powered by OpenAI and NewsAPI")
