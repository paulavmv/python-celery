from flask import Flask, request
from .worker import create_app
from .business.hard_work import send_email, strings_to_upper

app = Flask(__name__)

create_app(app)

@app.route('/send_email', methods=['POST'])
def email_notification():

    send_email.delay()

    return {'message': 'Email sent.'}

@app.route('/upperfy', methods=['POST'])
def notification():
    text = request.json['text']
    upper_text = strings_to_upper(text)

    return {'upper_text': upper_text}

