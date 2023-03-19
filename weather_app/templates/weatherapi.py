import datetime as dt
import requests

BASE_URL = "http://api.weatherstack.com/current?"
access_key = "563c23c12a9ec70164fb29149ca891f1"
CITY = "New York"


def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9 / 5) + 32

    return celsius, fahrenheit


url = BASE_URL + "access_key=" + access_key + "&query=" + CITY
response = requests.get(url).json()

visibility = response['current']['visibility']
feelsLike = response['current']['feelsLike']
humidity = response['current']['humidity']
precip = response['current']['precip']
wind_dir = response['current']['wind_dir']
weather_descriptions = response['current']['weather_descriptions']
weather_code = response['current']['weather_code']
temperature = response['current']['temperature']
observation_time = response['current']['observation_time']
weather_icon = response['current']['weather_icon']

print(visibility)

#temp_kelvin = response['main']['temp']
#temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)