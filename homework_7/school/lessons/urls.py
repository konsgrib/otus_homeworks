from django.urls import path
from . import views

urlpatterns = [
    path("", views.lessons, name="lessons"),
    path("lesson/<int:pk>/", views.lesson, name="lesson"),
    path("create-lesson", views.create_lesson, name="create-lesson"),
    path("update-lesson/<int:pk>/", views.update_lesson, name="update-lesson"),
    path("delete-lesson/<int:pk>/", views.delete_lesson, name="delete-lesson"),
]
