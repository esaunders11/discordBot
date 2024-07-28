#import my libraries and API key
import discord
from googlesearch import search
import KEY
import time

TOKEN = KEY.DISCORD_TOKEN

#set my bots intents and privilages
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

#message showing the bot is online
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

#event handler for when a message is send in the server
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    results = ""
    msg = message.content

    #scrapes google for the first 5 urls attached to the message that is given and sends them in the channel
    if message.content[0] == "!":
        for res in search(msg, tld="co.in", num=5, stop=5, pause=4):
            results += res + "\n"

        time.sleep(1)

        await message.channel.send(results)

    
#connects bot to server using API key
client.run(TOKEN)
