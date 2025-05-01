# Adding Error Handling and Logging
import logging
import requests

# Set up logging
logging.basicConfig(level=logging.INFO)

api_key = 'your_api_key_here'
url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad HTTP status codes
    
    data = response.json()
    articles = data['articles']

    for article in articles:
        print(f"Headline: {article['title']}")
        print(f"Source: {article['source']['name']}")
        print(f"URL: {article['url']}")
        print("-" * 80)

except requests.exceptions.RequestException as e:
    logging.error(f"Error fetching news: {e}")
except KeyError as e:
    logging.error(f"Error parsing response: Missing key {e}")
