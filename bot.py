import discord
from googlesearch import search
import KEY
import time

TOKEN = KEY.DISCORD_TOKEN


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    results = ""
    msg = message.content

    if message.content[0] == "!":
        for res in search(msg, tld="co.in", num=5, stop=5, pause=4):
            results += res + "\n"

        time.sleep(1)
    
        await message.channel.send(results)

    




client.run(TOKEN)
