from django.db import models
from products.models import (
    Product,
)


class SchoolGroup(models.Model):
    title = models.CharField(max_length=100)
    teacher = models.ForeignKey("users.Teacher", on_delete=models.CASCADE)
    type = models.ForeignKey("GroupType", on_delete=models.CASCADE)
    city = models.ForeignKey("products.City", on_delete=models.CASCADE)
    duration = models.IntegerField(null=False)
    invoice_string = models.CharField(max_length=200)
    student = models.ManyToManyField("users.Student", blank=True)
    product = models.ManyToManyField("products.Product", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.city}: {self.title}: {self.duration}"


class GroupType(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.title}: {self.description}"


class Lesson(models.Model):
    date_scheduled = models.DateTimeField()
    teacher = models.ForeignKey("users.Teacher", on_delete=models.CASCADE)
    group = models.ForeignKey("SchoolGroup", on_delete=models.CASCADE)
    student = models.ManyToManyField("users.Student", blank=True)
    topic = models.CharField(max_length=300)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}: {self.date_scheduled.strftime('%Y-%m-%d')}: {self.teacher.user.first_name}{self.teacher.user.last_name} - {self.group.title} //{self.topic}//"

    class Meta:
        ordering = ["date_scheduled", "teacher"]
