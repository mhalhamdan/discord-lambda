import discord
from credentials import DISCORD_TOKEN

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    pass

client.run(DISCORD_TOKEN)