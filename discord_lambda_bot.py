import os
from io import BytesIO
import discord
from discord import Intents, Message
from function_manager import FunctionManager
from credentials import DISCORD_TOKEN
from constants import VALID_COMMANDS

client = discord.Client(intents=Intents.all())

function_manager = FunctionManager()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message: Message) -> None:
    pass
    

client.run(DISCORD_TOKEN)