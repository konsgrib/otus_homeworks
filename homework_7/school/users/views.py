from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Customer, Student
from .forms import StudentForm, CustomerForm

# from .forms import ProductForm


def teachers(request):
    return render(request, "teachers/teachers.html")


def students(request):
    students = Student.objects.all()
    context = {"type": "student", "objects": students}
    return render(request, "users/list.html", context)


def student(request, pk):
    student = Student.objects.get(id=pk)
    context = {"object": student, "type": "student"}
    return render(request, "users/user.html", context)


def create_student(request):
    form = StudentForm()

    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("students")

    context = {"form": form, "type": "student"}
    return render(request, "users/user_form.html", context)


def update_student(request, pk):
    student = Student.objects.get(id=pk)
    form = StudentForm(instance=student)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("students")

    context = {"form": form, "type": "student"}
    return render(request, "users/user_form.html", context)


def delete_student(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == "POST":
        student.delete()
        return redirect("students")
    context = {"object": student, "type": "student"}
    return render(request, "delete_template.html", context)


def customers(request):
    customers = Customer.objects.all()
    context = {"type": "customer", "objects": customers}
    return render(request, "users/list.html", context)


def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    context = {"object": customer, "type": "customer"}
    return render(request, "users/user.html", context)


def create_customer(request):
    form = CustomerForm()

    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("customers")

    context = {"form": form, "type": "customer"}
    return render(request, "users/user_form.html", context)


def update_customer(request, pk):
    customer = Customer.objects.get(id=pk)
    form = CustomerForm(instance=customer)

    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect("customers")

    context = {"form": form, "type": "customer"}
    return render(request, "users/user_form.html", context)


def delete_customer(request, pk):
    customer = Customer.objects.get(id=pk)
    if request.method == "POST":
        customer.delete()
        return redirect("customers")
    context = {"object": customer, "type": "customer"}
    return render(request, "delete_template.html", context)
