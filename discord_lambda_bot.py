import logging
import discord
from discord import Intents, Message
from function_manager import FunctionManager
from discord_lambda_utils import validate_args, parse_message, execute_command
from credentials import LambdaBot
from constants import *


# Create instance of the client
client = discord.Client(intents=Intents.all())

# Create instance of the function manager
function_manager = FunctionManager()

async def handle_message(message: Message) -> str:
    tokens, command = parse_message(message)

    validate_args(command, len(tokens))

    return await execute_command(function_manager, command, tokens, message.attachments)

# Log that the bot connected
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

# Process messages and commands
@client.event
async def on_message(message: Message) -> None:
    # Inital checks
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
        response = await handle_message(message)
        print(response)
        await message.channel.send(response)
    except (ValueError, FileExistsError, FileNotFoundError) as err:
        await message.channel.send(err)
    except Exception as err:
        await message.channel.send("Encountered an unknown error, check the logs for more information.")
        logging.error(err)

    return

client.run(LambdaBot)