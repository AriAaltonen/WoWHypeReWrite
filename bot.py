import discord
import datetime
import os

token = os.environ.get('token')
client = discord.Client()
client.run(token)
