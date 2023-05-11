from .celery_app import app as celery_app

# чтобы аппка стартонула вместе с нашим приложением

__all__ = ('celery_app',)
