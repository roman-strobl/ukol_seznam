from django.apps import AppConfig


class BackedConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backed'

    def ready(self):

        from .task import start_downloader

        start_downloader()
        