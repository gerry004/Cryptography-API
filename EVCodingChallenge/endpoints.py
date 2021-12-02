from flask import Blueprint, request, jsonify
import os
from cryptography.fernet import Fernet

bp = Blueprint('endpoints', __name__, url_prefix="/")
# encryption_key = Fernet.generate_key()

encryption_key = b'W8R5MesHZCOgPaWKL37vslY_YvwDjKQVU0kEegHEHPk='
fernet = Fernet(encryption_key)

@bp.route('encrypt', methods=('POST',))
def encrypt():
    data = request.get_json()
    encrypted_data = {}
    for key in data:
        encrypted_data[key] = fernet.encrypt(str(data[key]).encode()).decode()
    return jsonify(data=encrypted_data), 200

@bp.route('decrypt', methods=('POST',))
def decrypt():
    data = request.get_json()
    decrypted_data = {} 
    for key in data:
        decrypted_data[key] = fernet.decrypt(str(data[key]).encode()).decode()
    return jsonify(data=decrypted_data), 200

@bp.route('sign')
def sign():
    return 'Sign Endpoint'

@bp.route('verify')
def verify():
    return 'Verify Endpoint'
