from django.urls import path
from . import views

urlpatterns = [
    path("", views.lessons, name="lessons"),
    path("lesson/<int:pk>/", views.lesson, name="lesson"),
    path("create-lesson", views.create_lesson, name="create-lesson"),
    path("update-lesson/<int:pk>/", views.update_lesson, name="update-lesson"),
    path("delete-lesson/<int:pk>/", views.delete_lesson, name="delete-lesson"),
    path("groups/", views.groups, name="groups"),
    path("get-group/<int:pk>/", views.get_group, name="get-group"),
    path("create-group", views.create_group, name="create-group"),
    path("update-group/<int:pk>/", views.update_group, name="update-group"),
    path("delete-group/<int:pk>/", views.delete_group, name="delete-group"),
]
