from flask import Blueprint, request, jsonify, current_app
from cryptography.fernet import Fernet
from CryptographyAPI.helpers import decrypt_json, standardize_json, compute_signature

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
    decrypted_data = decrypt_json(data)
    
    return jsonify(decrypted_data), 200

@bp.route('sign', methods=('POST',))
def sign():
    data = request.get_json()
    signed_data = {}

    signed_data['data'] = decrypt_json(data)
    standardized_json = standardize_json(data)
    signed_data["signature"] = compute_signature(standardized_json)

    return jsonify(signed_data), 200

@bp.route('verify', methods=('POST',))
def verify():
    data = request.get_json()

    decrypted_data = decrypt_json(data['data'])
    standardized_json = standardize_json(decrypted_data)

    signature = compute_signature(standardized_json)

    if signature == data['signature']:
        return jsonify(), 204
    
    return jsonify(), 400
