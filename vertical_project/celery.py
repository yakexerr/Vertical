import os
from celery import Celery

# Устанавливаем переменную окружения, чтобы Celery знал, где искать настройки Django.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vertical_project.settings')

# Создаем экземпляр приложения Celery
app = Celery('vertical_project')

# Загружаем конфигурацию из настроек Django.
# Celery будет искать все настройки, которые начинаются с "CELERY_"
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически находить все файлы tasks.py в наших приложениях.
app.autodiscover_tasks()