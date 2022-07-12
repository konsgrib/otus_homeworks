from django.urls import path
from .views import (
    LessonListView,
    LessonDetailView,
    LessonCreateView,
    LessonUpdateView,
    LessonDeleteView,
    SchoolGroupListView,
    SchoolGroupDetailView,
    SchoolGroupCreateView,
    SchoolGroupUpdateView,
    SchoolGroupDeleteView,
)

urlpatterns = [
    path("", LessonListView.as_view(), name="lessons"),
    path("lesson/<int:pk>/", LessonDetailView.as_view(), name="lesson"),
    path("create-lesson", LessonCreateView.as_view(), name="create-lesson"),
    path("update-lesson/<int:pk>/", LessonUpdateView.as_view(), name="update-lesson"),
    path("delete-lesson/<int:pk>/", LessonDeleteView.as_view(), name="delete-lesson"),
    path("groups/", SchoolGroupListView.as_view(), name="groups"),
    path("get-group/<int:pk>/", SchoolGroupDetailView.as_view(), name="get-group"),
    path("create-group", SchoolGroupCreateView.as_view(), name="create-group"),
    path(
        "update-group/<int:pk>/", SchoolGroupUpdateView.as_view(), name="update-group"
    ),
    path(
        "delete-group/<int:pk>/", SchoolGroupDeleteView.as_view(), name="delete-group"
    ),
]
