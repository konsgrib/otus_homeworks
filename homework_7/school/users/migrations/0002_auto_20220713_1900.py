# Generated by Django 3.2.2 on 2022-07-13 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baseuser',
            name='user_name',
        ),
        migrations.AlterField(
            model_name='baseuser',
            name='username',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]