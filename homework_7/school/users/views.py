from django.shortcuts import render, redirect
from django.http import HttpResponse
import time

from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView


from .models import Customer, Student
from .forms import StudentForm, CustomerForm

from .tasks import send_mail_task
from school.celery import school_app

def mailer(request):
    task_id = None

    if request.method=="POST":
        print(time.time())
        task = send_mail_task.delay("subject","test_test")
        print(time.time())
        task_id = task.id
    context = {"task_id":task_id}

    return render(request,"users/mail.html",context=context)


def status_view(request, task_id):  
    print(task_id)
    task = school_app.AsyncResult(task_id)
    print(f'result: {task.result}')
    context = {'task_id': task_id,
               'status': task.status}

    return render(request, 'users/status.html', context=context)








class StudentListView(ListView):
    model = Student
    paginate_by = 10


class StudentDetailView(DetailView):
    model = Student


class StudentCreateView(CreateView):
    model = Student
    fields = (
        "first_name",
        "last_name",
        "email",
        "phone",
        "ssn",
        "bound_customer",
    )


class StudentUpdateView(UpdateView):
    model = Student
    fields = (
        "first_name",
        "last_name",
        "email",
        "phone",
        "ssn",
        "bound_customer",
    )


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy("students")


class CustomerListView(ListView):
    model = Customer


class CustomerDetailView(DetailView):
    model = Customer


class CustomerCreateView(CreateView):
    model = Customer
    fields = (
        "first_name",
        "last_name",
        "email",
        "phone",
        "ssn",
        "want_invoice",
    )


class CustomerUpdateView(UpdateView):
    model = Customer
    fields = (
        "first_name",
        "last_name",
        "email",
        "phone",
        "ssn",
        "want_invoice",
    )


class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = reverse_lazy("customers")
