from django.apps import AppConfig
class OperationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'operation'
    
    def ready(self):
        from .threaded_task import run_task_periodically
        run_task_periodically(30)

