import pyowm
import json
import requests
from bot import Bot
from Database_connection import Database_connection
from time import sleep
import Imagedownloader as imgdl

class Weatherbot(Bot):

    def __init__(self, bot_id, bot_password, url_base, city):
        super().__init__(bot_id, bot_password, url_base)
        self.city = city
        self.owm = pyowm.OWM('bf4a53760aec2ae431890bb6d7766337')
        self.wm = self.owm.weather_manager()
        self.db = Database_connection("Weatherbot.db")
        self.db.create_table("Posts", "id INTEGER PRIMARY KEY, post_id INTEGER, city TEXT")
        self.db.create_table("Comments", "id INTEGER PRIMARY KEY, comment_id INTEGER, post_id INTEGER, city TEXT")


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
        #imgdl.getImages returns a list of images, so we need to get the first one
        #this following database request is to prevent the bot from posting the same image twice
        post_ids = self.db.select("Posts", "post_id", "city='"+city+"'")
        print(post_ids)
        if len(post_ids) < 3:
            images = imgdl.getImages(city, 3, 1, "images")
            image = images[len(post_ids)]
            print(len(post_ids))
        else:
             images = imgdl.getImages(city, len(post_ids), 1, "images")
             image = images[len(post_ids)-1]
        #image is the path to the image on the bot's computer
        post_id = self.create_post(post_text=text, hashtags="#weather #"+city, image=image)
        self.db.insert("Posts", "post_id, city", str(post_id)+", '"+city+"'")
        return post_id

weatherbot = Weatherbot(6, "123456", "http://192.168.2.33:5000/", "Berlin")
print("Weatherbot started")
weatherbot.post_weather()
'''

while True:
    post_ids = weatherbot.db.select("Posts", "post_id", "1=1")
    print(post_ids)
    for post_id in post_ids:
        if post_id[0] > 0:
            print(post_id[0])
            comments = weatherbot.get_comments(post_id[0])
            print(comments)
            size = len(comments)
            if size > 0:
                if comments[size-1]["text"] == "weather":
                    weather = weatherbot.whichweathertoday(weatherbot.city)
                    text = "Weather in " + weatherbot.city + " has " + weather.detailed_status + " and temperature is " + str(weather.temperature('celsius')['temp']) + "°C at the moment."
                    weatherbot.db.insert("Comments", "comment_id, post_id, city", str(comments[size-1]["id"]+1)+", "+str(post_id[0])+", '"+weatherbot.city+"'")
                    weatherbot.create_comment(post_id[0], text)
        else:
            print("This post don't exist anymore")
    sleep(2) # Sleep for 60 seconds
'''