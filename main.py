import requests
import json
import os
from bot import Bot

# Create a bot
bot1 = Bot(5, "123456", "http://192.168.2.33:5000/")
bot1.login()
print(bot1.get_posts())
bot1.get_post(8)
bot1.get_comments(8)
bot1.like_post(8)
bot1.create_comment(8, "Now, the bot is commenting on his own post")
print("---Class Bot is working---")


