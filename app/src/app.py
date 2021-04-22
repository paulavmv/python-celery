from flask import Flask
from .worker import create_app

app = Flask(__name__)

create_app(app)

@app.route('/')
def hello_world():
    return 'Hello World'


