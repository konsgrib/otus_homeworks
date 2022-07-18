from django.urls import path, include
from . import views
from .views import (
    StudentListView,
    StudentDetailView,
    StudentCreateView,
    StudentUpdateView,
    StudentDeleteView,
    CustomerListView,
    CustomerDetailView,
    CustomerCreateView,
    CustomerUpdateView,
    CustomerDeleteView,
    status_view,
    mailer,
)

urlpatterns = [
    path("students/", StudentListView.as_view(), name="students"),
    path("student/<int:pk>/", StudentDetailView.as_view(), name="student"),
    path("create-student/", StudentCreateView.as_view(), name="create-student"),
    path(
        "update-student/<int:pk>/", StudentUpdateView.as_view(), name="update-student"
    ),
    path(
        "delete-student/<int:pk>/", StudentDeleteView.as_view(), name="delete-student"
    ),
    path("customers/", CustomerListView.as_view(), name="customers"),
    path("customer/<int:pk>/", CustomerDetailView.as_view(), name="customer"),
    path("create-customer/", CustomerCreateView.as_view(), name="create-customer"),
    path(
        "update-customer/<int:pk>/",
        CustomerUpdateView.as_view(),
        name="update-customer",
    ),
    path(
        "delete-customer/<int:pk>/",
        CustomerDeleteView.as_view(),
        name="delete-customer",
    ),
    path("logon/", include("django.contrib.auth.urls")),

    path('mail/', mailer),
    path('status/<str:task_id>/', status_view, name='status_view'),
    
]
