from django.forms import (
    ModelForm,
    Form,
    CharField,
    TextInput,
    EmailField,
    Textarea,
)

from django.core.mail import send_mail
from .models import Student, Customer, FeedbackMessage
from .tasks import send_email_job,save_message,send_reply_email

class ContactForm(Form):
    name = CharField(
        label="Your name",
        widget=TextInput(
            attrs={
                "class": "form-control mb-3",
                "placeholder": "name",
                "id": "form-firstname",
            }
        ),
    )

    message = CharField(
        label="Message",
        widget=Textarea(
            attrs={"class": "form-control mb-3", "rows": "5", "id": "form-message"}
        ),
    )

    email = EmailField(
        label="E-mail",
        max_length=200,
        widget=TextInput(
            attrs={
                "class": "form-control mb-3",
                "placeholder": "email",
                "id": "form-email",
            }
        ),
    )

    def send_mail(self):
        send_email_job.delay(
            self.cleaned_data["name"],
            self.cleaned_data["message"],
            self.cleaned_data["email"],
        )

    def store_message_form(self):
        save_message.delay(
            self.cleaned_data["name"],
            self.cleaned_data["message"],
            self.cleaned_data["email"],
        )

    def reply_mail(self):
        send_reply_email.delay(
            self.cleaned_data["name"],
            self.cleaned_data["email"],
        )


class StudentForm(ModelForm):
    class Meta:
        model = Student
        # fields = "__all__"
        fields = ("first_name", "last_name")


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
