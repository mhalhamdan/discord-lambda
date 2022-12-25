import os
from io import BytesIO
import discord
from discord import Intents, Message
from function_manager import FunctionManager
from discord_lambda_utils import validate_args, handle_message
from credentials import LambdaBot
from constants import *

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
    if not message.content:
        return
    # Do not let the bot reply to itself
    if message.author == client.user:
        return

    # Convert content to lowercase
    message.content = message.content.lower()

    # Check if the prefix was called
    if not message.content.startswith(BOT_COMMAND_PREFIX):
        return
    
    try:
        msg, command = handle_message(message)
    except ValueError as err:
        await message.channel.send(err)

    try:
        validate_args(command, len(msg))
    except ValueError as err:
        await message.channel.send(err)

    # Retrieve function name after validating arguments
    function_name = msg[FUNCTION_NAME_INDEX]

    if command == 'create':
        function_manager.create_function(function_name)
        await message.channel.send(f'function {function_name} created')

    elif command == 'deploy':
        # Check an attachment was provided
        if len(message.attachments) != 1:
            await message.channel.send(f'Please provide one zip folder as an attachment that includes requirements.txt and a python file')
            return
        zip_folder = BytesIO()
        await message.attachments[0].save(zip_folder)
        function_manager.deploy_function(function_name, zip_folder)

    elif command == 'rename':
        new_func_name = msg[NEW_NAME_INDEX]
        function_manager.rename_function(function_name, new_func_name)

    elif command == 'delete':
        function_manager.delete_function(function_name)

    elif command == 'run':
        args = msg[RUN_ARGS_INDEX:]
        function_manager.run_function(function_name, args)

    # Exit processing this message
    return


client.run(LambdaBot)