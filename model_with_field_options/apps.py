from django.apps import AppConfig


class ModelWithFieldOptionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'model_with_field_options'
