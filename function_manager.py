import os
import shutil
from io import BytesIO
from zipfile import ZipFile

class FunctionManager(object):
    def __init__(self, FUNCTIONS_ROOT_DIR="functions") -> None:
        self.FUNCTIONS_ROOT_DIR = FUNCTIONS_ROOT_DIR 

        if not os.path.isdir(FUNCTIONS_ROOT_DIR):
            os.mkdir(self.FUNCTIONS_ROOT_DIR)

    def create_function(self, function_name: str) -> None:
        function_path = os.path.join(self.FUNCTIONS_ROOT_DIR, function_name)
        if os.path.isdir(function_path):
            raise FileExistsError(f"Function {function_name} already exists.")

        os.mkdir(function_path)

    def deploy_function(self, function_name: str, zip_folder: BytesIO) -> None:
        function_path = os.path.join(self.FUNCTIONS_ROOT_DIR, function_name)
        if not os.path.isdir(function_path):
            raise FileNotFoundError(f"Function {function_name} does not exist.")
        
        # Delete existing folder to overwrite
        shutil.rmtree(function_path)

        os.mkdir(function_path)

        with ZipFile(zip_folder, 'r') as zip_object:
            zip_object.extractall(function_path)

    def run_function(self, function_name: str) -> None:
        pass
    
    def rename_function(self, function_name: str, new_function_name: str) -> None:
        # Check if old path actually exists
        function_path = os.path.join(self.FUNCTIONS_ROOT_DIR, function_name)
        if not os.path.isdir(function_path):
            raise FileNotFoundError(f"Function {function_name} does not exist.")

        # Check if new path already exists
        new_function_path = os.path.join(self.FUNCTIONS_ROOT_DIR, new_function_name)
        if os.path.isdir(new_function_path):
            raise FileExistsError(f"Function {new_function_name} already exists.")

        os.rename(function_path, new_function_path)

    def delete_function(self, function_name: str) -> None:
        function_path = os.path.join(self.FUNCTIONS_ROOT_DIR, function_name)
        if not os.path.isdir(function_path):
            raise FileNotFoundError(f"Function {function_name} does not exist.")
        
        shutil.rmtree(function_path)


if __name__ == "__main__":
    pass