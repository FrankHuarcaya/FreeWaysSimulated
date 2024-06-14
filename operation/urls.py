# operation/urls.py
from django.urls import path
from .views import calculate_pressure_simulated,AverageVehiclePerDayReport,TrafficFlowReport,TrafficLightApi,AvenueApi,IntersectionApi,LaneGroupApi, TrafficPredicctionAPI,TrafficFlowApi
from . import views


urlpatterns = [

    path('trafficflows/', TrafficFlowApi.as_view(), name='trafficflows-list'),
    path('trafficflows/<int:id>/', TrafficFlowApi.as_view(), name='trafficflow-detail'),

    path('trafficlights/', TrafficLightApi.as_view(), name='traffic_light_api'),
    path('trafficlights/<int:id>/', TrafficLightApi.as_view(), name='traffic_light_api_detail'),

    path('predictions/', TrafficPredicctionAPI.as_view(), name='traffic_predictions'),

    path('avenue/', AvenueApi.as_view(), name='avenue_list'),
    path('avenue/<int:id>/', AvenueApi.as_view(), name='avenue_detail'),
    path('intersection/', IntersectionApi.as_view(), name='intersection_list'),
    path('intersection/<int:id>/', IntersectionApi.as_view(), name='intersection_detail'),
    path('lane-group/', LaneGroupApi.as_view(), name='lane_group_list'),
    path('lane-group/<int:id>/', LaneGroupApi.as_view(), name='lane_group_detail'),

 
    path('traffic-flow-report/<str:intersection_name>/', TrafficFlowReport.as_view(), name='traffic_flow_report'),
    path('average-vehicle-per-day-report/<str:intersection_name>/', AverageVehiclePerDayReport.as_view(), name='average_vehicle_per_day_report'),
    path('calculate_pressure_simulated/<int:intersection_id>/', calculate_pressure_simulated, name='calculate_pressure_simulated'),

]