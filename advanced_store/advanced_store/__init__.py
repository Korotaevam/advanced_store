# для того чтобы console работала по проекту в консоле import advanced_store, ниже настройки для этого
import os

import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'advanced_store.settings'
django.setup()
