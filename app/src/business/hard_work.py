from ..worker import celery
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)


@celery.task(bind=True)
def send_email(task):
    logger.info('Send email')
    #implement process to send email

