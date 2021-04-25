from ..worker import celery
from celery.utils.log import get_task_logger
from celery import group


logger = get_task_logger(__name__)


@celery.task(bind=True)
def send_email(task):
    logger.info('Send email')
    #implement process to send email


def strings_to_upper(text):
    upper_text = group(strings_to_upper_task.s(line)
                    for line in text.split('.'))().get()
    return '.'.join(upper_text)


@celery.task(bind=True)
def strings_to_upper_task(task, text):
    logger.info('To upper: {0}'.format(text))
    return text.upper()
