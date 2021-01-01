import discord
import os
import requests
import json

client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + "\n - " + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  print('{0.user} is alive!'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('quote'):
    quote = get_quote()
    await message.channel.send(quote)

client.run(os.getenv('TOKEN'))
