# Generated by Django 3.2.2 on 2022-07-13 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("users", "0001_initial"),
        ("lessons", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="schoolgroup",
            name="student",
            field=models.ManyToManyField(blank=True, to="users.Student"),
        ),
        migrations.AddField(
            model_name="schoolgroup",
            name="teacher",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="users.teacher"
            ),
        ),
        migrations.AddField(
            model_name="schoolgroup",
            name="type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="lessons.grouptype"
            ),
        ),
        migrations.AddField(
            model_name="lesson",
            name="group",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="lessons.schoolgroup"
            ),
        ),
        migrations.AddField(
            model_name="lesson",
            name="student",
            field=models.ManyToManyField(blank=True, to="users.Student"),
        ),
        migrations.AddField(
            model_name="lesson",
            name="teacher",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="users.teacher"
            ),
        ),
    ]
