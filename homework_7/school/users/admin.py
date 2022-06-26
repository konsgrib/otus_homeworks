from django.contrib import admin

from .models import (
    Teacher,
    Customer,
    Student,
)

admin.site.register(Customer)
admin.site.register(Student)
admin.site.register(Teacher)
