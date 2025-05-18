from django.apps import AppConfig
import json
import threading
import time

"""def run_task_loop():
    from b_serverbas.tasks import check_tache_alerts  # Import here to avoid circular import issues
    while True:
        print("Running task...")
        check_tache_alerts()  # Call the function
        print("Task completed.")
        time.sleep(3600)  # Run every 1 hour
"""
class BServerbasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'b_serverbas'

    def ready(self):
        import b_serverbas.signals

        #thread = threading.Thread(target=run_task_loop, daemon=True)
        #thread.start()