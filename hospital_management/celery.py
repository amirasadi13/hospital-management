from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hospital_management.settings")
app = Celery("hospital_management", backend='')
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
