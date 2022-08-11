from django.apps import AppConfig


class PreviewerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'previewer'

    def ready(self):
        from . import signals