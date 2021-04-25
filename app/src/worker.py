from celery import Celery
import os

#get the message broker url
redis_url = os.environ.get("REDIS_URL", 'redis://localhost:6379')

celery = Celery(__name__, backend="%s/0" % redis_url, broker="%s/1" % redis_url,
                include=('app.src.business.hard_work',))


def create_app(app):
    celery.conf.update(app.config)
