import os

class FunctionManager(object):
    def __init__(self, ROOT_DIR="functions") -> None:
        self.ROOT_DIR = ROOT_DIR

    def create_function(self, function_name: str):
        pass

    def deploy_function(self, function_name: str, zip_folder: str):
        pass

    def run_function(self, function_name: str):
        pass
    
    def rename_function(self, function_name: str, new_function_name: str):
        pass

    def delete_function(self, function_name: str):
        pass

if __name__ == "__main__":
    pass