# python-celery

This project refers to a quick tutorial on how to use Python + Flask + Celery
It requires redis or some other message broker to be running.

Starting the project:


export FLASK_APP=app/src/app.py

python3 -m flask run

celery -A app.src.worker worker -l info

