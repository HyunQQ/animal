
from django.apps import AppConfig

class AppConfig(AppConfig):
    name = 'app'

    def ready(self):
        from config import app_config
        app_config.AppConfig()