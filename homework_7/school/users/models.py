from django.db import models

from django.contrib.auth.models import User

from lessons.models import Product


class Teacher(models.Model):
    """
    Class describing teachers
    """

    user = models.OneToOneField(User, on_delete=models.PROTECT, null=True)
    ssn = models.CharField(max_length=12)
    phone = models.CharField(max_length=13)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.id}: {self.user.last_name} {self.user.first_name}"

    class Meta:
        ordering = ["user"]


class Customer(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    ssn = models.CharField(max_length=12)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    want_invoice = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id}: {self.last_name} {self.name}: {self.phone}: {self.email}"


class Student(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    ssn = models.CharField(max_length=12)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id}: {self.last_name} {self.name}: {self.phone}: {self.email}"
