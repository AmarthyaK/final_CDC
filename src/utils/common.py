from src.logger import logging
from pathlib import Path
import sys
import os
from src.exception import CustomException
from box import ConfigBox

import boto3

import urllib.request as request
import zipfile

from box.exceptions import BoxValueError
import yaml

from ensure import ensure_annotations


# reading yaml file
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    #except BoxValueError:
        #raise ValueError("yaml file is empty")
    except Exception as e:
        raise CustomException(e,sys)

#Creating directories
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logging.info(f"created directory at: {path}")

#Downloading zip files

def download_zip_files(local_data_file: Path, source_url: str):

    if not os.path.exists(local_data_file):
        logging.info("Inside download function")
        filename, headers = request.urlretrieve(source_url, local_data_file)
        logging.info(f"downloaded file: {filename}")
    else:
        logging.info(f"file: {local_data_file} already exists")

#Unzipping zip files
def unzip_zip_files(local_data_file: Path, unzip_dir: Path):

    logging.info("Inside unzip function")
    with zipfile.ZipFile(local_data_file, 'r') as zip_ref:
        zip_ref.extractall(unzip_dir)
    logging.info(f"unzipped file: {local_data_file}")


#downloading s3 buckets

def download_s3(local_data_file: Path):
    try:
        s3 = boto3.resource(
        service_name='s3',
        region_name='us-east-2',
        aws_access_key_id='AKIA6MIKGRKFH4QA3J75',
        aws_secret_access_key='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'
        )
        if not os.path.exists(local_data_file):
            logging.info("Inside download function")
            s3.Bucket('chickenfecalimgs').download_file(Key = 'Chicken_fecal_imgs.zip', Filename = local_data_file)
            logging.info(f"downloaded s3 data successfully: {local_data_file}")
        else:
            logging.info(f"file: {local_data_file} already exists")

    
    except Exception as e:
        raise CustomException(e,sys)