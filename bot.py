from secret import token
import discord

client = discord.Client()


@client.event
async def on_message(message):
    print(message.content)
    if message.content.find("!hello") != -1:
        await message.channel.send("Hi")
        
client.run(token)
