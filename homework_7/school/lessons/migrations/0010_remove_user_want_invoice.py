# Generated by Django 3.2 on 2022-06-21 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0009_rename_ptroducttype_producttype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='want_invoice',
        ),
    ]
