import os
import requests
from dotenv import load_dotenv

load_dotenv()
NEWS_API_KEY = os.getenv('NEWS_API_KEY')

def fetch_news(category):
    url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={NEWS_API_KEY}&country=us'
    response = requests.get(url)
    if response.status_code == 200:
        print("News fetched successfully.")
        return response.json()['articles']
    else:
        print(f"Error fetching news: {response.status_code}")
        return []
