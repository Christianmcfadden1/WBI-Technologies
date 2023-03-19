from flask import Flask, render_template
import datetime as dt
import requests
import random as random

BASE_URL = "http://api.weatherstack.com/current?"
access_key = "563c23c12a9ec70164fb29149ca891f1"
CITY = "New York"
unit = "f"




def get_weather():
    response = random.randint(1,100)
    ##url = BASE_URL + "access_key=" + access_key + "&query=" + CITY + "&units=" + unit
    ##response = requests.get(url).json()
    return response

response = get_weather()

print(response)

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'bdufhsbd'

    @app.route('/')
    def home():
        visibility = response['current']['visibility']
        feelsLike = response['current']['feelslike']
        humidity = response['current']['humidity']
        precip = response['current']['precip']
        wind_dir = response['current']['wind_dir']
        weather_descriptions = response['current']['weather_descriptions']
        weather_code = response['current']['weather_code']
        temperature = response['current']['temperature']
        observation_time = response['current']['observation_time']
        weather_icon = response['current']['weather_icons']

        return render_template("home.html", city=CITY, visibility=visibility, feelsLike=feelsLike, humidity=humidity, precip=precip, wind_dir=wind_dir, weather_descriptions=weather_descriptions, weather_code=weather_code, temperature=temperature, observation_time=observation_time, weather_icon=weather_icon)
    
    return app



app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

