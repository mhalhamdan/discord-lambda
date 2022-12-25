from discord import Message
from constants import *

def handle_message(message: Message) -> tuple:
    # Lower the message content
    message.content = message.content.lower()

    msg = message.content.split()

    # Check if the command is valid
    try:
        command = msg[COMMAND_INDEX]
    except IndexError:
        raise ValueError(f"No command was provided. Please use one of these commands {VALID_COMMANDS}.'")
    if not command in VALID_COMMANDS:
        raise ValueError(f'command **{command}** not valid. Please use one of these commands {VALID_COMMANDS}.')

    return msg, command
    

def validate_args(command: str, msg_size: int) -> None:
    if command == 'create':
        if msg_size != CREATE_ARG_SIZE:
            message = 'command **CREATE** correct format is **<-fn> <create> <function name>**. Example: -fn create bur3i'
            raise ValueError(message)

    elif command == 'deploy':
        if msg_size != DEPLOY_ARG_SIZE:
            message = 'command **DEPLOY** correct format is **<-fn> <deploy> <function name>**. Example: -fn deploy bur3i'
            raise ValueError(message)

    elif command == 'rename':
        if msg_size != RENAME_ARG_SIZE:
            message = 'command **RENAME** correct format is **<-fn> <rename> <old function name> <new function name>**. Example: -fn rename bur3i bur2i'
            raise ValueError(message)

    elif command == 'delete':
        if msg_size != DELETE_ARG_SIZE:
            message = 'command **DELETE** correct format is **<-fn> <delete> <function name>**. Example: -fn delete bur3i'
            raise ValueError(message)

    elif command == 'run':
        if msg_size > RUN_MIN_ARG_SIZE:
            message = 'command **run** correct format is **<-fn> <run> <function name> <arg1> <arg2> ...**. Example: -fn run add 3 5 98 1'
            raise ValueError(message)
 