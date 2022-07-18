import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "school.settings")

school_app = Celery("school", backend="rpc://")
school_app.config_from_object("django.conf:settings", namespace="CELERY")
school_app.autodiscover_tasks()
