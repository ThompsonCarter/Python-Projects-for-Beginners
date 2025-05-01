import requests

# Function to get weather data
def get_weather(city, api_key):
    # OpenWeatherMap API endpoint
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    # Send a GET request to the API
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        
        # Extract relevant data from the response
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        city_name = data["name"]
        
        # Return the weather information
        return f"The weather in {city_name} is {description} with a temperature of {temperature}°C."
    else:
        return "Error: Could not retrieve weather data."

# Main function
def main():
    api_key = "your_api_key_here"  # Replace with your actual API key
    city = input("Enter the city: ")
    
    weather_info = get_weather(city, api_key)
    print(weather_info)

# Run the app
main()
