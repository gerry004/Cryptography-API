from flask import Flask
from EVCodingChallenge import endpoints
from cryptography.fernet import Fernet

def create_app():

    app = Flask(__name__)
    app.register_blueprint(endpoints.bp)

    encryption_key = Fernet.generate_key()
    fernet = Fernet(encryption_key)

    return app

# f = open("ev-coding-challenge-env/bin/activate", "a")
# print(f.write('adding to activate file'))

# read_file = open("ev-coding-challenge-env/bin/activate", "r")
# print(read_file.read())

# os.environ['ENCRYPTION_KEY'] = encryption_key.decode()
# with open (os.path.relpath('/EVCodingChallenge/endpoints.py', start=os.curdir), 'r') as outfile:
#     data = outfile.read()
#     print(data)