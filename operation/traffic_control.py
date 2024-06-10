import random
import logging
from .models import Intersection, Avenue, TrafficLight, LaneGroup

import logging

def calculate_green_time(pressures):
    total_pressure = sum([pressure[1] for pressure in pressures])
    green_time_1 = max(30, min(150, int((pressures[0][1] / total_pressure) * 180)))
    green_time_2 = max(30, 180 - green_time_1)  # Garantizar que la suma sea 180 segundos y no sea menor a 30
    logging.info(f"Calculated green times: {green_time_1}, {green_time_2} for pressures: {pressures}")
    return green_time_1, green_time_2

def calculate_red_time(green_times):
    red_time_1 = max(30, 180 - green_times[0])
    red_time_2 = max(30, 180 - green_times[1])
    logging.info(f"Calculated red times: {red_time_1}, {red_time_2} for green times: {green_times}")
    return red_time_1, red_time_2
