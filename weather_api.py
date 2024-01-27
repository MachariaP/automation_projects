#!/usr/bin/env python3
import requests

# API key for accessing the OpenWeatherMap API
api_key = "9a00936e375fd7d8f1bb95513c24fc89"
# API endpoint URL for weather data
api_url = "https://api.openweathermap.org/data/2.5/weather"

# User input for the city
city = input("Write your city: ")

# Sending a GET request to OpenWeatherMap API
response = requests.get(
        url=api_url,
        params={
            "q": city,
            "appid": api_key,
            "units": "metric"
            }
        )

# Parsing the response JSON data
weather_data = response.json()

# Displaying the temparature for the specified city
print(city, "temperature is" ,weather_data['main']['temp'])
