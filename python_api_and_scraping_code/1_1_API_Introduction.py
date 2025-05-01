# What is an API?
# APIs (Application Programming Interfaces) are a set of rules that allow different software applications to communicate with each other.
# Many websites and services provide APIs that allow you to access their data programmatically.

# Example: Fetching data from an API
import requests

# API endpoint
url = "https://jsonplaceholder.typicode.com/posts"

# Send a GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Parse the JSON data from the response
    print(data)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
