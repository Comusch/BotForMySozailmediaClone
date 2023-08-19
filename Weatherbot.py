import pyowm
import json
import requests
from bot import Bot

class Weatherbot(Bot):

    def __init__(self, bot_id, bot_password, url_base, city):
        super().__init__(bot_id, bot_password, url_base)
        self.city = city
        self.owm = pyowm.OWM('bf4a53760aec2ae431890bb6d7766337')
        self.wm = self.owm.weather_manager()

    def whichweathertoday(self, city=""):
        if city == "":
            city = self.city
        location = self.wm.weather_at_place(city)
        weather = location.weather
        return weather

    def post_weather(self, city=""):
        if city == "":
            city = self.city
        weather = self.whichweathertoday(city)  # Corrected typo here
        text = "Weather in " + city + " has " + weather.detailed_status+" and temperature is "+str(weather.temperature('celsius')['temp'])+"°C at the moment."
        return self.create_post(post_text=text, hashtags="#weather #"+city)

weatherbot = Weatherbot(6, "123456", "http://192.168.2.33:5000/", "Munich")
weatherbot.post_weather()