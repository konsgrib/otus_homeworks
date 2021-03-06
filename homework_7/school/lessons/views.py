from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Lesson, SchoolGroup


class LessonListView(ListView):
    model = Lesson
    page_title = "lessons"

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.select_related("group", "teacher")
        return qs


class LessonDetailView(DetailView):
    model = Lesson


class LessonCreateView(CreateView):
    model = Lesson
    fields = "__all__"


class LessonUpdateView(UpdateView):
    model = Lesson
    fields = "__all__"

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     qs = qs.select_related("group")
    #     return qs


class LessonDeleteView(DeleteView):
    model = Lesson
    success_url = reverse_lazy("lessons")


class SchoolGroupListView(ListView):
    model = SchoolGroup


class SchoolGroupDetailView(DetailView):
    model = SchoolGroup


class SchoolGroupCreateView(CreateView):
    model = SchoolGroup
    fields = "__all__"


class SchoolGroupUpdateView(UpdateView):
    model = SchoolGroup
    fields = "__all__"


class SchoolGroupDeleteView(DeleteView):
    model = SchoolGroup
    success_url = reverse_lazy("groups")
