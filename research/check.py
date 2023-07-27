from src.exception import CustomException
from src.logger import logging

import sys

try:
    from src.utils.common import read_yaml,create_directories
    from src.constants import constant_paths
except Exception as e:
    raise CustomException(e,sys)

if __name__ == "__main__":
    logging.info("create_directories loaded successfully")
    cp = constant_paths()
    a,b = cp.get_paths()
    print(a,b)