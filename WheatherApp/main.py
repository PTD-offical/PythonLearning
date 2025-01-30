import requests


# Variables
API_key = "28c33bce3b6c64c0f8b7834c5b8e3bc9"
UsrInput = input("Enter City Name: ")

WeatherData = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + UsrInput + "&appid=" + API_key)

print(WeatherData.json())
Weather = WeatherData.json()["weather"][0]["main"]
Temp = round(WeatherData.json()["main"]["temp"])

print(f"Current Weather in {UsrInput} is {Weather} and the temperature is {Temp}°C")