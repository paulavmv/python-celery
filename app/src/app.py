from flask import Flask, request
from .worker import create_app
from .business.hard_work import send_email

app = Flask(__name__)

create_app(app)

@app.route('/send_email', methods=['POST'])
def replace():

    result = send_email.delay()

    return {'message': 'Email sent.'}


