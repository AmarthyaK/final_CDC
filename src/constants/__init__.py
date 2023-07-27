from pathlib import Path


#config and params file paths

CONFIG_FILE_PATH = Path("config/config.yaml")
PARAMS_FILE_PATH = Path("params.yaml")

class constant_paths:
    def __init__(self):
        self.CONFIG_FILE_PATH = CONFIG_FILE_PATH
        self.PARAMS_FILE_PATH = PARAMS_FILE_PATH
    def get_paths(self):
        return self.CONFIG_FILE_PATH, self.PARAMS_FILE_PATH
