from flask import Blueprint

bp = Blueprint('endpoints', __name__, url_prefix="/")

@bp.route('encrypt')
def encrypt():
    return 'Encrypt Endpoint'

@bp.route('decrypt')
def decrypt():
    return 'Decrypt Endpoint'

@bp.route('sign')
def sign():
    return 'Sign Endpoint'

@bp.route('verify')
def verify():
    return 'Verify Endpoint'