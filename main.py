import requests
import json
import os
from bot import Bot

# Create a bot
bot1 = Bot(5, "123456", "http://192.168.2.33:5000/")
bot1.login()
bot1.change_Description("This is the first functional bot! However, it is not very smart yet.")

