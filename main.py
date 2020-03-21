import discord
from discord.ext import tasks

TOKEN = ''
CHANNEL_ID = '690802888846344233'

client = discord.Client()


@client.event
async def on_ready():
    print('ログインしました')
    channel = client.get_channel(CHANNEL_ID)
    print(channel)


client.run(TOKEN)
