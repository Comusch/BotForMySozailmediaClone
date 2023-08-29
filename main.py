import requests
import json
import os
from bot import Bot

#DONE: Create a save system for the bot which posts he wrote and which comments he wrote --> DONE
#DONE: Implement a nural network which classifies text into classes (e.g. weather, news, etc.) --> DONE
#Done: Add a image api to insert images into the posts --> DONE
#TODO: Create a function that the weather bot comments on the comments under his posts (e.g. "for this city i can also tell you the weather")
#TODO: Add a function that the weather bot tells the weather for a city every day in the hashtag #weather


# Create a bot
bot1 = Bot(5, "123456", "http://192.168.2.33:5000/")
bot1.login()
print(bot1.get_posts())
bot1.get_post(8)
bot1.get_comments(8)
bot1.like_post(8)
bot1.create_comment(8, "Now, the bot is commenting on his own post")
print("---Class Bot is working---")


