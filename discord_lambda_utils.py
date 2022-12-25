from io import BytesIO
from discord import Message, Attachment
from function_manager import FunctionManager
from constants import *


def parse_message(message: Message) -> tuple:
    tokens = message.content.split()

    # Check if the command is valid
    try:
        command = tokens[COMMAND_INDEX]
    except IndexError:
        raise ValueError(f"No command was provided. Please use one of these commands {VALID_COMMANDS}.'")
    if not command in VALID_COMMANDS:
        raise ValueError(f'command **{command}** not valid. Please use one of these commands {VALID_COMMANDS}.')

    return tokens, command


async def execute_command(function_manager: FunctionManager, command: str, tokens: list, attachments: list = None) -> str:
 # Retrieve function name after validating arguments
    function_name = tokens[FUNCTION_NAME_INDEX]

    if command == 'create':
        function_manager.create_function(function_name)
        return f'function {function_name} created successfully.'

    elif command == 'deploy':
        # Check an attachment was provided
        if not attachments:
            raise ValueError(f'Please provide one zip folder as an attachment that includes requirements.txt and a python file')
        zip_folder = BytesIO()
        await attachments[0].save(zip_folder)
        function_manager.deploy_function(function_name, zip_folder)
        return f'function {function_name} deployed successfully.'

    elif command == 'rename':
        new_func_name = tokens[NEW_NAME_INDEX]
        function_manager.rename_function(function_name, new_func_name)
        return f'function {function_name} renamed to {new_func_name} successfully.'

    elif command == 'delete':
        function_manager.delete_function(function_name)
        return f'function {function_name} deleted successfully.'

    elif command == 'run':
        args = tokens[RUN_ARGS_INDEX:]
        output = function_manager.run_function(function_name, args)
        return f'Output of {function_name}: {output}'


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
        if not msg_size >= RUN_MIN_ARG_SIZE:
            message = 'command **run** correct format is **<-fn> <run> <function name> <arg1> <arg2> ...**. Example: -fn run add 3 5 98 1'
            raise ValueError(message)
 