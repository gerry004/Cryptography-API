## EV-Coding-Challenge
## Setting Up Python Virtual Environment
python3 -m venv ev-coding-challenge-env

source ev-coding-challenge-env/bin/activate

## How to Execute Program
pip install -e .

export FLASK_APP=EVCodingChallenge

export FLASK_ENV=development

flask run

## Making Requests to Endpoints Using Curl in Bash Terminal
curl localhost:5000/encrypt -d '{"string data": "foobar", "boolean data": "True", "integer data": "178"}' -H 'Content-Type: application/json'

curl localhost:5000/decrypt -d '{"boolean data": "gAAAAABhqTliMJ4HtqixayMqyNnHY9dM3fqr3xAbpMcxhUnR2XKxYmhp8xSuctzwCWxPvOnYBDYjT7nBpDpZ6hyehX8ycJXqOg==", "integer data": "gAAAAABhqTliwteCByXIvU_arxmkTysD9atWMK8F_olkZ-9pZPXxQaAm9WfJK8DiQB8tmiev1G6o4F567NUX_Hl5SqOKHFaK7g==", "string data": "gAAAAABhqTliZsPeSWuFNmRNCnI8X0pybUG_GVOXFLiyCCJBWOc1_ivbgEF8QyA9QHbZOwqVJYiRBgf7HMNk1fh-1PSQAheFMQ=="}' -H 'Content-Type: application/json'