from django.template import Context
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from .models import FeedbackMessage

def send_contacts_email(name, message, email):
    context = {
        "name": name,
        "message": message,
        "email": "admin@test.com",
    }

    email_subject = "Contact form"
    email_body = render_to_string("users/email_msg.txt", context)

    email = EmailMessage(
        email_subject,
        email_body,
        settings.DEFAULT_FROM_EMAIL,
        [
            email,
        ],
    )
    return email.send(fail_silently=False)


def reply_email(name, email):
    context = {
        "name": name,
        "email": email,
    }
    print(context)
    email_subject = "Reply"
    email_body = render_to_string("users/response.txt", context)

    email = EmailMessage(
        email_subject,
        email_body,
        settings.DEFAULT_FROM_EMAIL,
        [
            email,
        ],
    )
    return email.send(fail_silently=False)   

def store_message(name,message,email):
    msg = FeedbackMessage(name=name,message=message,email=email)
    msg.save()
    return msg.pk