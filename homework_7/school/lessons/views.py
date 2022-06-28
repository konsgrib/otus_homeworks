from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import LessonForm, GroupForm

from .models import Lesson, SchoolGroup


def lessons(request):
    lessons = Lesson.objects.all()
    context = {
        "lessons": lessons,
    }
    return render(request, "lessons/lessons.html", context)


def lesson(request, pk):
    lesson = Lesson.objects.get(id=pk)
    context = {"lesson": lesson}
    return render(request, "lessons/lesson.html", context)


def create_lesson(request):
    form = LessonForm()

    if request.method == "POST":
        form = LessonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lessons")
    context = {"form": form}
    return render(request, "lessons/lesson_form.html", context)


def update_lesson(request, pk):
    lesson = Lesson.objects.get(id=pk)
    form = LessonForm(instance=lesson)

    if request.method == "POST":
        form = LessonForm(request.POST, instance=lesson)
        if form.is_valid():
            form.save()
            return redirect("lessons")

    context = {"form": form}
    return render(request, "lessons/lesson_form.html", context)


def delete_lesson(request, pk):
    lesson = Lesson.objects.get(id=pk)
    if request.method == "POST":
        lesson.delete()
        return redirect("lessons")
    context = {"object": lesson, "type": "lesson"}
    return render(request, "delete_template.html", context)


def groups(request):
    groups = SchoolGroup.objects.all()
    context = {
        "groups": groups,
    }
    return render(request, "groups/groups.html", context)


def get_group(request, pk):
    group = SchoolGroup.objects.get(id=pk)
    context = {"group": group}
    return render(request, "groups/group.html", context)


def create_group(request):
    form = GroupForm()

    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("groups")
    context = {"form": form}
    return render(request, "groups/group_form.html", context)


def update_group(request, pk):
    group = SchoolGroup.objects.get(id=pk)
    form = GroupForm(instance=group)

    if request.method == "POST":
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect("groups")

    context = {"form": form}
    return render(request, "groups/group_form.html", context)


def delete_group(request, pk):
    group = SchoolGroup.objects.get(id=pk)
    if request.method == "POST":
        group.delete()
        return redirect("groups")
    context = {"object": group, "type": "group"}
    return render(request, "delete_template.html", context)
