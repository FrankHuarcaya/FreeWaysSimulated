# operation/threaded_task.py

import threading
import time
from .tasks import update_traffic_lights_simulated

def run_task_periodically(interval):
    def task_wrapper():
        while True:
            update_traffic_lights_simulated()
            time.sleep(interval)

    task_thread = threading.Thread(target=task_wrapper)
    task_thread.daemon = True
    task_thread.start()

# Llama a esta función con el intervalo deseado en segundos
