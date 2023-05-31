from django.apps import AppConfig


class PageProfileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'page_profile'

    def ready(self):
        import page_profile.signals