# Fetching Data from an API in Python
import requests

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    # Print the title of the first post
    print(data[0]['title'])
else:
    print(f"Error: {response.status_code}")
