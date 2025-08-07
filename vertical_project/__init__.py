# Этот код гарантирует, что наше приложение Celery будет загружено,
# когда Django стартует.
from .celery import app as celery_app

__all__ = ('celery_app',)
