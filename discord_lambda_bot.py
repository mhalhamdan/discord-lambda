import os
from io import BytesIO
import discord
from discord import Intents, Message
from function_manager import FunctionManager
from credentials import LambdaBot
from constants import VALID_COMMANDS

# Set prefix for the bot
PREFIX = '-fn'

# Create instance of the client
client = discord.Client(intents=Intents.all())

# Create instance of the function manager
function_manager = FunctionManager()

# Log that the bot connected
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

# Process messages and commands
@client.event
async def on_message(message: Message) -> None:
    # Lower the message content
    message.content = message.content.lower()
    # Do not let the bot reply to itself
    if message.author == client.user:
        return
    # Split the message
    msg = message.content.split()
    # Check if the prefix was called and handle command
    if PREFIX == msg[0]:
        # Check if the command is valid
        command = msg[1]
        if command in VALID_COMMANDS:
            # Process create
            if command == 'create':
                # Check if message is the correct length
                if len(msg) != 3:
                    await message.channel.send(f'command **CREATE** correct format is **<-fn> <create> <function name>**. Example: -fn create bur3i')
                    return
                # Create function
                funcname = msg[2]
                function_manager.create_function(funcname)
                await message.channel.send(f'function {funcname} created')
            # Process deploy
            if command == 'deploy':
                # Check if message is the correct length
                if len(msg) != 3:
                    await message.channel.send(f'command **DEPLOY** correct format is **<-fn> <deploy> <function name>**. Example: -fn deploy bur3i')
                    return
                # Deploy function

            # Exit processing this message
            return
    # Send that the command is not valid
    await message.channel.send(f'command **{command}** not valid. Please use one of these commands {VALID_COMMANDS}.')
    
    

client.run(LambdaBot)