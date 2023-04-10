# для того чтобы console работала по проекту в консоле import advanced_store, ниже настройки для этого
import os
from .celery import app as celery_app
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'advanced_store.settings'
django.setup()

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.


__all__ = ('celery_app',)
