import os, json
from flask import Flask
from EVCodingChallenge import endpoints
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

    # json_data = {
    #     'what': 'the',
    #     'hell': {
    #         'is': 'this',
    #         'huh': '?'
    #     }
    # }
    # print(json_data)
    # for key in json_data:
    #     if type(json_data[key]) == dict:
    #         print(json_data[key])

    # string_json = "{'what': 'the', 'hell': {'is': 'this', 'huh': '?'}}"
    # string_json = string_json.replace("'", '"')
    # json_string = json.loads(string_json)
    # print(json_string)
    # print(json_string['hell'])

    
    app.register_blueprint(endpoints.bp)

    return app
