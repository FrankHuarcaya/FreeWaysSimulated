# operation/tasks.py

from .views import calculate_pressure_simulated
from .models import Intersection




def update_traffic_lights_simulated():
    from django.test import RequestFactory
    factory = RequestFactory()
    request = factory.get('/fake-path/')
    intersections = Intersection.objects.all()
    for intersection in intersections:
        calculate_pressure_simulated(request, intersection.id)




