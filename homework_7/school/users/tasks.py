from time import sleep
from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_mail_task(subject,message):
    sleep(15)
    send_mail(subject,message,"from@example.com",
    ["to@example.com"], fail_silently=False)