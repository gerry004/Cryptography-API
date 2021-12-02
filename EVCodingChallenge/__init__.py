from flask import Flask
from EVCodingChallenge import endpoints


def create_app():

    app = Flask(__name__)
    app.register_blueprint(endpoints.bp)

    return app