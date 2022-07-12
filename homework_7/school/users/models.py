from django.db import models

from django.contrib.auth.models import User

from lessons.models import Product


class BaseUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, null=True)
    ssn = models.CharField(max_length=12)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.id}: {self.user.last_name} {self.user.first_name}"


class Teacher(BaseUser):
    class Meta:
        ordering = ["user"]


class Customer(BaseUser):
    want_invoice = models.BooleanField(default=True)


class Student(BaseUser):
    bound_customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
