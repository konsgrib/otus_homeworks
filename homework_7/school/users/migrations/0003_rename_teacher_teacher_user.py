# Generated by Django 3.2.2 on 2022-06-25 23:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220626_0139'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='teacher',
            new_name='user',
        ),
    ]