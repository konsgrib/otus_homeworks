from django.forms import ModelForm, DateField, DateInput


from .models import Lesson


class LessonForm(ModelForm):
    date_scheduled = DateField(
        widget=DateInput(format=("%Y-%m-%d"), attrs={"type": "date"}), required=True
    )

    class Meta:
        model = Lesson
        fields = "__all__"
