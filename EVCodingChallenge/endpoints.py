from flask import Blueprint, request, jsonify, current_app
from cryptography.fernet import Fernet

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
    fernet = Fernet(current_app.config['ENCRYPTION_KEY'])

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
