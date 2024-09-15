from django.apps import AppConfig

class DemoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'demo'

    def ready(self):
        import demo.signals  # Importing signals to ensure they are registered
