from flask import Blueprint, request, jsonify, current_app
from cryptography.fernet import Fernet
import json
from hashlib import sha256

bp = Blueprint('endpoints', __name__, url_prefix="/")

@bp.route('encrypt', methods=('POST',))
def encrypt():
    data = request.get_json()
    fernet = Fernet(current_app.config['ENCRYPTION_KEY'])

    for key in data:
        data[key] = fernet.encrypt(str(data[key]).encode()).decode()

    return jsonify(data), 200

@bp.route('decrypt', methods=('POST',))
def decrypt():
    data = request.get_json()
    decrypted_data = decrypt_json(data, "gAAAAABhq")
    
    return jsonify(decrypted_data), 200

@bp.route('sign', methods=('POST',))
def sign():
    data = request.get_json()
    signed_data = {}
    signed_data['data'] = decrypt_json(data, "gAAAAABhq")
    standardized_json = standardize_json(data)

    print(standardized_json)
    signed_data["signature"] = compute_signature(standardized_json)

    return jsonify(signed_data), 200

@bp.route('verify', methods=('POST',))
def verify():
    data = request.get_json()

    decrypted_data = decrypt_json(data['data'], "gAAAAABhq")
    standardized_json = standardize_json(decrypted_data)

    print(standardized_json)
    signature = compute_signature(standardized_json)

    if signature == data['signature']:
        return jsonify(), 204
    
    return jsonify(initial=data['signature'], computed=signature), 400

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
    sorted_dict = {}
    
    for i in sorted(data):
        sorted_dict[i] = data[i]

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
