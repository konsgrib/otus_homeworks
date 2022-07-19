from time import sleep
from celery import shared_task
from django.core.mail import send_mail

from .email import send_contacts_email, store_message, reply_email
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task
def send_mail_task(subject, message):
    sleep(15)
    send_mail(
        subject, message, "from@example.com", ["to@example.com"], fail_silently=False
    )


@shared_task
def send_email_job(name, message, email):
    logger.info("Mail sent to admin")
    return send_contacts_email(name, message, email)


@shared_task
def send_reply_email(name, email):
    logger.info(f"Reply sent to: {name}, {email}")
    return reply_email(name, email)


@shared_task
def save_message(name, message, email):
    logger.info("Message stored into db")
    return store_message(name, message, email)