import os
import discord
from random import choice
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('.mock'):
    sentence = message.content
    print(sentence)
    new = sentence.replace(".mock", " ")
    mock = ''.join(choice((str.upper, str.lower))(c) for c in new)

    # await message.delete()
    await message.channel.send(mock)

client.run(os.getenv('TOKEN'))
