import os

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

    def deploy_function(self, function_name: str, zip_folder: str) -> None:
        pass

    def run_function(self, function_name: str) -> None:
        pass
    
    def rename_function(self, function_name: str, new_function_name: str) -> None:
        pass

    def delete_function(self, function_name: str) -> None:
        pass

if __name__ == "__main__":
    pass