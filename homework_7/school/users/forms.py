from django.forms import ModelForm

from .models import Student, Customer


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = "__all__"


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
