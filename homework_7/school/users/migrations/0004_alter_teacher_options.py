# Generated by Django 3.2.2 on 2022-06-26 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_teacher_teacher_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teacher',
            options={'ordering': ['user']},
        ),
    ]
