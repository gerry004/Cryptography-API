from flask import Blueprint, request, jsonify, current_app
from cryptography.fernet import Fernet
import json

bp = Blueprint('endpoints', __name__, url_prefix="/")
fernet = Fernet('GAVHRmNp3uqui4I0bQ7zP8S2FJrO6e9ZRB1BKwA05vM=')

@bp.route('encrypt', methods=('POST',))
def encrypt():
    data = request.get_json()
    # fernet = Fernet(current_app.config['ENCRYPTION_KEY'])

    for key in data:
        if type(data[key]) == dict: 
            print(data[key])
            data[key] = standardize_json(data[key])
            print(data[key])
            data[key] = fernet.encrypt(str(data[key]).encode()).decode()
        else:
            data[key] = fernet.encrypt(str(data[key]).encode()).decode()

    return jsonify(data), 200

@bp.route('decrypt', methods=('POST',))
def decrypt():
    data = request.get_json()
    # fernet = Fernet(current_app.config['ENCRYPTION_KEY'])

    for key in data:
        if data[key].startswith("gAAAAABhq") == True:
            data[key] = fernet.decrypt(str(data[key]).encode()).decode()
    
    return jsonify(data), 200

@bp.route('sign', methods=('POST',))
def sign():
    fernet = Fernet(current_app.config['ENCRYPTION_KEY'])
    data = request.get_json()
    signed_data = {}

    for key in data['data']:
        if data['data'][key].startswith("gAAAAABhq") == True:
            data['data'][key] = fernet.decrypt(str(data['data'][key]).encode()).decode()

    signed_data['data'] = data
    signed_data["signature"] = fernet.encrypt(str(data).encode()).decode()

    return jsonify(signed_data), 200

@bp.route('verify', methods=('POST',))
def verify():
    fernet = Fernet(current_app.config['ENCRYPTION_KEY'])
    data = request.get_json()

    for key in data['data']:
        if data['data'][key].startswith("gAAAAABhq") == True:
            data['data'][key] = fernet.decrypt(str(data['data'][key]).encode()).decode()
    
    computed_signature = fernet.encrypt(str(data['data']).encode()).decode()

    if computed_signature == data['signature']:
        print(data['signature'], 'initial signature')
        print(computed_signature, 'computed signature')
        print('verified')
        return 204
    
    return jsonify(data), 400

def standardize_json(data: dict) -> str:
    sorted_dict = {}
    
    for i in sorted(data):
        sorted_dict[i] = data[i]

    string = str(sorted_dict)
    string = string.replace("'", '"')
    string = string.replace(" ", "")

    return string

def convert_string_to_json(string: str) -> dict:
    string = string.replace("'", '"')
    json_data = json.loads(string)
    return json_data

def decrypt_values(data: dict, indicator: str) -> dict:
    fernet = Fernet(current_app.config['ENCRYPTION_KEY'])

    for key in data:
        if data[key].startswith(indicator) == True:
            data[key] = fernet.decrypt(str(data[key]).encode()).decode()
    
    return data

# curl localhost:5000/encrypt -d '{"string data": {"barfoo": "money", "foobar": "honey"}, "boolean data": "True", "integer data": "178"}' -H 'Content-Type: application/json'