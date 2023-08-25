from django.apps import AppConfig


class ModelWithMetaClassConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'model_with_meta_class'
