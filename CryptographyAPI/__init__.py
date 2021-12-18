import os
from flask import Flask
from CryptographyAPI import endpoints
from cryptography.fernet import Fernet

def create_app():

    app = Flask(__name__)

    if os.path.exists('key.key'):
        with open("key.key", "r") as key_file:
            app.config['ENCRYPTION_KEY'] = key_file.read()
    else:
        with open("key.key", "w") as key_file:
            encryption_key = Fernet.generate_key()
            key_file.write(encryption_key.decode())
    
    app.register_blueprint(endpoints.bp)

    return app
