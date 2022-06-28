from django.forms import ModelForm, DateField, DateInput


from .models import Lesson, SchoolGroup


class LessonForm(ModelForm):
    date_scheduled = DateField(
        widget=DateInput(format=("%Y-%m-%d"), attrs={"type": "date"}), required=True
    )

    class Meta:
        model = Lesson
        fields = "__all__"


class GroupForm(ModelForm):
    class Meta:
        model = SchoolGroup
        fields = "__all__"
