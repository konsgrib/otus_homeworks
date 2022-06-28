from django.urls import path
from . import views

urlpatterns = [
    path("students/", views.students, name="students"),
    path("student/<int:pk>/", views.student, name="student"),
    path("create-student/", views.create_student, name="create-student"),
    path("update-student/<int:pk>/", views.update_student, name="update-student"),
    path("delete-student/<int:pk>/", views.delete_student, name="delete-student"),
    path("customers/", views.customers, name="customers"),
    path("customer/<int:pk>/", views.customer, name="customer"),
    path("create-customer/", views.create_customer, name="create-customer"),
    path("update-customer/<int:pk>/", views.update_customer, name="update-customer"),
    path("delete-customer/<int:pk>/", views.delete_customer, name="delete-customer"),
]
