## EV-Coding-Challenge
## Setting Up Python Virtual Environment
python3 -m venv cryptography-api-env

source cryptography-api-env/bin/activate

## How to Execute Program
pip install -e .

export FLASK_APP=CryptographyAPI

export FLASK_ENV=development

flask run

## Making Requests to Endpoints Using Curl in Bash Terminal
In the form:

curl localhost:5000/endpoint-name -d '{ "json": "data" }' -H 'Content-Type: application/json'

Example:

curl localhost:5000/encrypt -d '{"name": "Bob", "age": "17", "address": { "line 1": "14 Street", "line 2": "Town Name", "line 3": "County" }}' -H 'Content-Type: application/json'
