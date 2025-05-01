# Code Explanation:

# Requests to Fetch Data:
# The requests.get(url) function sends an HTTP GET request to the OpenWeatherMap API,
# using the URL constructed with the provided city name and API key.

# Handling the Response:
# The response from the API is a JSON object. We use response.json() to parse it into a Python dictionary.
# The temperature and weather description are extracted from the response using dictionary keys.

# Displaying the Weather:
# The weather data is formatted and printed in a human-readable format.
# If the API call fails, an error message is displayed.
