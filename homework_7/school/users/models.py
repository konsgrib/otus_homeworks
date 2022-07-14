from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

from django.urls import reverse

from django.contrib.auth.models import BaseUserManager


class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, user_name, first_name, password, **other_fields):

        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be assigned to is_staff=True")

        if other_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must be assigned to is_superuser=True")

        if other_fields.get("is_active") is not True:
            raise ValueError("Superuser must be assigned to is_active=True")

        return self.create_user(email, user_name, first_name, password, **other_fields)

    def create_user(self, email, user_name, first_name, password, **other_fields):
        if not email:
            raise ValueError(_("Please provide an email address"))
        email = self.normalize_email(email)
        user = self.model(
            email=email, user_name=user_name, first_name=first_name, **other_fields
        )
        user.set_password(password)
        user.save()


class BaseUser(AbstractUser):

    username = models.CharField(max_length=150, unique=True, blank=False)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    ssn = models.CharField(max_length=12)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
        "ssn",
        "phone",
        "email",
    ]

    def __str__(self):
        return f"{self.id}: {self.last_name} {self.first_name}"


class Teacher(BaseUser):
    def get_absolute_url(self):
        return reverse("teacher", kwargs={"pk": self.pk})


class Customer(BaseUser):
    want_invoice = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("customer", kwargs={"pk": self.pk})


class Student(BaseUser):
    bound_customer = models.ForeignKey("Customer", on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("student", kwargs={"pk": self.pk})
