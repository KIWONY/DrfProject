from django.apps import AppConfig


class DrfbackendConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'drfbackend'

    def ready(self):
        import drfbackend.signals