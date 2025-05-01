# Hands-On Project: Build a Program that Fetches the Latest News Headlines Using an API
import requests

# Your NewsAPI key (replace with your own key)
api_key = 'your_api_key_here'

# NewsAPI endpoint for top headlines
url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    articles = data['articles']

    for article in articles:
        print(f"Headline: {article['title']}")
        print(f"Source: {article['source']['name']}")
        print(f"URL: {article['url']}")
        print("-" * 80)
else:
    print(f"Failed to fetch news: {response.status_code}")
