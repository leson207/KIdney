import os
import yaml
import json
import joblib
import base64
from typing import Any
from pathlib import Path
from box import ConfigBox
from box.exceptions import BoxValueError
from ensure import ensure_annotations

from Kidney import logger


@ensure_annotations
def read_yaml(path: Path) -> ConfigBox:
    try:
        with open(path) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f'yaml file: {path} loaded successfully')
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError('Yaml file is empty')
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(paths: list, verbose=True):
    for path in paths:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f'Create directory at {path}')

@ensure_annotations
def save_json(path: Path, data: dict):
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)
    
    logger.info(f'Json file saved at: {path}')

@ensure_annotations
def save_bin(data: any, path: Path):
    joblib.dump(value=data, filename=path)
    logger.info(f'Binary file saved at: {path}')

@ensure_annotations
def load_bin(path: Path) -> Any:
    data = joblib.load(path)
    logger.info(f'Binary file loaded from: {path}')
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    size_in_kb = round(os.path.getsize(path)/1024)
    return f'~ {size_in_kb} KB'

@ensure_annotations
def decode_image(img_string, file_name):
    img_data = base64.b64decode(img_string)
    with open(file_name, 'wb') as f:
        f.write(img_data)
        f.close()

@ensure_annotations
def encodeImageToBase64(path):
    with open(path, 'rb') as f:
        return base64.b64encode(f.read())