# Web Scraping with BeautifulSoup
import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all the headlines
    headlines = soup.find_all('h3')
    
    for headline in headlines:
        print(headline.text)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
