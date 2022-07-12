from django.shortcuts import render, redirect
from django.http import HttpResponse


from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView


from .models import Customer, Student
from .forms import StudentForm, CustomerForm


class StudentListView(ListView):
    model = Student


class StudentDetailView(DetailView):
    model = Student


class StudentCreateView(CreateView):
    model = Student
    fields = "__all__"


class StudentUpdateView(UpdateView):
    model = Student
    fields = "__all__"


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy("students")


class CustomerListView(ListView):
    model = Customer


class CustomerDetailView(DetailView):
    model = Customer


class CustomerCreateView(CreateView):
    model = Customer
    fields = "__all__"


class CustomerUpdateView(UpdateView):
    model = Customer
    fields = "__all__"


class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = reverse_lazy("customers")
