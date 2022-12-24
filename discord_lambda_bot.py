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
                func_name = msg[2]
                function_manager.create_function(func_name)
                await message.channel.send(f'function {func_name} created')
            # Process deploy
            elif command == 'deploy':
                # Check if message is the correct length
                if len(msg) != 3:
                    await message.channel.send(f'command **DEPLOY** correct format is **<-fn> <deploy> <function name>**. Example: -fn deploy bur3i')
                    return
                # Check an attachment was provided
                if len(message.attachments) != 1:
                    await message.channel.send(f'Please provide one zip folder as an attachment that includes requirements.txt and a python file')
                    return
                # Deploy function
                zip_folder = BytesIO()
                func_name = msg[2]
                await message.attachments[0].save(zip_folder)
                await FunctionManager.deploy_function(func_name, zip_folder)
            # Process rename
            elif command == 'rename':
                # Check if message is the correct length
                if len(msg) != 4:
                    await message.channel.send(f'command **RENAME** correct format is **<-fn> <rename> <old function name> <new function name>**. Example: -fn rename bur3i yessir')
                    return
                # Rename function
                old_func_name = msg[2]
                new_func_name = msg[3]
                await FunctionManager.rename_function(old_func_name, new_func_name)
            # Process delete
            elif command == 'delete':
                # Check if message is the correct length
                if len(msg) != 3:
                    await message.channel.send(f'command **DELETE** correct format is **<-fn> <delete> <function name>**. Example: -fn delete bur3i')
                    return
                # Delete function
                func_name = msg[2]
                await FunctionManager.delete_function(func_name)
            # Process run
            elif command == 'run':
                # Check if message is the correct length
                if len(msg) > 3:
                    await message.channel.send(f'command **run** correct format is **<-fn> <run> <function name> <arg1> <arg2> ...**. Example: -fn run add 3 5 98 1')
                    return
                # Run function
                func_name = msg[2]
                args = msg[3:]
                await FunctionManager.run_function(func_name, args)
            # Exit processing this message
            return
    # Send that the command is not valid
    await message.channel.send(f'command **{command}** not valid. Please use one of these commands {VALID_COMMANDS}.')
    
    

client.run(LambdaBot)