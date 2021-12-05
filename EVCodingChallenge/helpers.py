import json
from cryptography.fernet import Fernet
from hashlib import sha256
from flask import current_app

def decrypt_json(data: dict, indicator: str) -> dict:
    fernet = Fernet(current_app.config['ENCRYPTION_KEY'])

    for key in data:
        if str(data[key]).startswith(indicator) == True:
            data[key] = fernet.decrypt(str(data[key]).encode()).decode()
            try:
                data[key] = convert_string_to_json(data[key])
            except Exception as e:
                print(e)
    
    return data

def standardize_json(data: dict) -> str:
    sorted_dict = sort_nested_json_by_key(data)

    string = str(sorted_dict)
    string = string.replace("'", '"')
    string = string.replace(" ", "")

    return string

def compute_signature(data: str) -> str: 
    signature = sha256(data.encode()).hexdigest()

    return signature

def convert_string_to_json(string: str) -> dict:
    string = string.replace("'", '"')
    json_data = json.loads(string)

    return json_data

def sort_nested_json_by_key(data: dict) -> dict:
    sorted_dict = {}
    
    for key in sorted(data):
        if type(data[key]) == dict:
            sorted_dict[key] = sort_nested_json_by_key(data[key])
        else:
            sorted_dict[key] = data[key]
    
    return sorted_dict