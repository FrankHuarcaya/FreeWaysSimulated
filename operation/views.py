
# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http import JsonResponse
from .serializers import TrafficFlowReadSerializer,TrafficFlowWriteSerializer,TrafficLightReadSerializer,TrafficLightWriteSerializer,AvenueSerializer,IntersectionSerializer,LaneGroupWriteSerializer,LaneGroupReadSerializer
from .models import TrafficLight
from operation.models import TrafficLight,Avenue,Intersection,LaneGroup,TrafficFlow
from security.permissions import IsAdminUser, IsMonitorUser, IsAnalystUser

# traffic/views.py

from django.http import JsonResponse



class TrafficLightApi(APIView):
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated, IsAdminUser]
        elif self.request.method == 'POST':
            self.permission_classes = [IsAuthenticated, IsAdminUser]
        elif self.request.method == 'PUT':
            self.permission_classes = [IsAuthenticated, IsAdminUser]
        elif self.request.method == 'DELETE':
            self.permission_classes = [IsAuthenticated, IsAdminUser]
        return super(TrafficLightApi, self).get_permissions()

    def get(self, request, id=0):
        if id > 0:
            traffic_light = TrafficLight.objects.get(id=id)
            traffic_light_serializer = TrafficLightReadSerializer(traffic_light)
            return Response(traffic_light_serializer.data)
        else:
            traffic_lights = TrafficLight.objects.all()
            traffic_light_serializer = TrafficLightReadSerializer(traffic_lights, many=True)
            return Response(traffic_light_serializer.data)

    def post(self, request):
        traffic_light_data = JSONParser().parse(request)
        traffic_light_serializer = TrafficLightWriteSerializer(data=traffic_light_data)
        if traffic_light_serializer.is_valid():
            traffic_light_serializer.save()
            return Response({"message": "Added Successfully"}, status=status.HTTP_201_CREATED)
        return Response({"message": "Failed to Add"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=0):
        traffic_light_data = JSONParser().parse(request)
        traffic_light = TrafficLight.objects.get(id=id)
        traffic_light_serializer = TrafficLightWriteSerializer(traffic_light, data=traffic_light_data)
        if traffic_light_serializer.is_valid():
            traffic_light_serializer.save()
            return Response({"message": "Updated Successfully"})
        return Response({"message": "Failed to Update"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=0):
        traffic_light = TrafficLight.objects.get(id=id)
        traffic_light.delete()
        return Response({"message": "Deleted Successfully"})
    


# Avenue
class AvenueApi(APIView):
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated, IsAdminUser]
        elif self.request.method == 'POST':
            self.permission_classes = [IsAuthenticated, IsAdminUser]
        elif self.request.method == 'PUT':
            self.permission_classes = [IsAuthenticated, IsAdminUser]
        elif self.request.method == 'DELETE':
            self.permission_classes = [IsAuthenticated, IsAdminUser]
        return super(AvenueApi, self).get_permissions()

    def get(self, request, id=0):
        if id > 0:
            avenue = Avenue.objects.get(id=id)
            avenue_serializer = AvenueSerializer(avenue)
            return Response(avenue_serializer.data)
        else:
            avenues = Avenue.objects.all()
            avenue_serializer = AvenueSerializer(avenues, many=True)
            return Response(avenue_serializer.data)
        
    def post(self, request):
        avenue_data = JSONParser().parse(request)
        avenue_serializer = AvenueSerializer(data=avenue_data)
        if avenue_serializer.is_valid():
            avenue_serializer.save()
            return Response({"message": "Added Successfully"}, status=status.HTTP_201_CREATED)
        return Response({"message": "Failed to Add"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=0):
        avenue_data = JSONParser().parse(request)
        avenue = Avenue.objects.get(id=id)
        avenue_serializer = AvenueSerializer(avenue, data=avenue_data)
        if avenue_serializer.is_valid():
            avenue_serializer.save()
            return Response({"message": "Updated Successfully"})
        return Response({"message": "Failed to Update"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=0):
        avenue = Avenue.objects.get(id=id)
        avenue.delete()
        return Response({"message": "Deleted Successfully"})


#Intersection

class IntersectionApi(APIView):
    permission_classes = [IsAuthenticated]

    
    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated, IsAdminUser]
        elif self.request.method == 'POST':
            self.permission_classes = [IsAuthenticated, IsAdminUser]
        elif self.request.method == 'PUT':
            self.permission_classes = [IsAuthenticated, IsAdminUser]
        elif self.request.method == 'DELETE':
            self.permission_classes = [IsAuthenticated, IsAdminUser]
        return super(IntersectionApi, self).get_permissions()

    def get(self, request, id=0):
        if id > 0:
            intersection = Intersection.objects.get(id=id)
            intersection_serializer = IntersectionSerializer(intersection)
            return Response(intersection_serializer.data)
        else:
            intersections = Intersection.objects.all()
            intersection_serializer = IntersectionSerializer(intersections, many=True)
            return Response(intersection_serializer.data)

    def post(self, request):
        intersection_data = JSONParser().parse(request)
        intersection_serializer = IntersectionSerializer(data=intersection_data)
        if intersection_serializer.is_valid():
            intersection_serializer.save()
            return Response({"message": "Added Successfully"}, status=status.HTTP_201_CREATED)
        return Response({"message": "Failed to Add"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=0):
        intersection_data = JSONParser().parse(request)
        intersection = Intersection.objects.get(id=id)
        intersection_serializer = IntersectionSerializer(intersection, data=intersection_data)
        if intersection_serializer.is_valid():
            intersection_serializer.save()
            return Response({"message": "Updated Successfully"})
        return Response({"message": "Failed to Update"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=0):
        intersection = Intersection.objects.get(id=id)
        intersection.delete()
        return Response({"message": "Deleted Successfully"})


#LaneGroup
class LaneGroupApi(APIView):
    permission_classes = [IsAuthenticated]
    
    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated, IsAdminUser]
        elif self.request.method == 'POST':
            self.permission_classes = [IsAuthenticated, IsAdminUser]
        elif self.request.method == 'PUT':
            self.permission_classes = [IsAuthenticated, IsAdminUser]
        elif self.request.method == 'DELETE':
            self.permission_classes = [IsAuthenticated, IsAdminUser]
        return super(LaneGroupApi, self).get_permissions()

    def get(self, request, id=0):
        try:
            if id > 0:
                lane_group = LaneGroup.objects.get(id=id)
                lane_group_serializer = LaneGroupReadSerializer(lane_group)
                return Response(lane_group_serializer.data)
            else:
                lane_groups = LaneGroup.objects.all()
                lane_group_serializer = LaneGroupReadSerializer(lane_groups, many=True)
                return Response(lane_group_serializer.data)
        except LaneGroup.DoesNotExist:
            return Response({"message": "LaneGroup not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        lane_group_data = JSONParser().parse(request)
        lane_group_serializer = LaneGroupWriteSerializer(data=lane_group_data)
        if lane_group_serializer.is_valid():
            lane_group_serializer.save()
            return Response({"message": "Added Successfully"}, status=status.HTTP_201_CREATED)
        return Response(lane_group_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=0):
        try:
            lane_group_data = JSONParser().parse(request)
            lane_group = LaneGroup.objects.get(id=id)
            lane_group_serializer = LaneGroupWriteSerializer(lane_group, data=lane_group_data)
            if lane_group_serializer.is_valid():
                lane_group_serializer.save()
                return Response({"message": "Updated Successfully"})
            return Response(lane_group_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except LaneGroup.DoesNotExist:
            return Response({"message": "LaneGroup not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, id=0):
        try:
            lane_group = LaneGroup.objects.get(id=id)
            lane_group.delete()
            return Response({"message": "Deleted Successfully"})
        except LaneGroup.DoesNotExist:
            return Response({"message": "LaneGroup not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TrafficFlowApi(APIView):
    permission_classes = [IsAuthenticated]
    
    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated, IsAdminUser]
        elif self.request.method == 'POST':
            self.permission_classes = [IsAuthenticated, IsAdminUser]
        elif self.request.method == 'PUT':
            self.permission_classes = [IsAuthenticated, IsAdminUser]
        elif self.request.method == 'DELETE':
            self.permission_classes = [IsAuthenticated, IsAdminUser]
        return super(TrafficFlowApi, self).get_permissions()

    def get(self, request, id=0):
        try:
            if id > 0:
                traffic_flow = TrafficFlow.objects.get(id=id)
                traffic_flow_serializer = TrafficFlowReadSerializer(traffic_flow)
                return Response(traffic_flow_serializer.data)
            else:
                traffic_flows = TrafficFlow.objects.all()
                traffic_flow_serializer = TrafficFlowReadSerializer(traffic_flows, many=True)
                return Response(traffic_flow_serializer.data)
        except TrafficFlow.DoesNotExist:
            return Response({"message": "TrafficFlow not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        traffic_flow_data = JSONParser().parse(request)
        traffic_flow_serializer = TrafficFlowWriteSerializer(data=traffic_flow_data)
        if traffic_flow_serializer.is_valid():
            traffic_flow_serializer.save()
            return Response({"message": "Added Successfully"}, status=status.HTTP_201_CREATED)
        return Response(traffic_flow_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=0):
        try:
            traffic_flow_data = JSONParser().parse(request)
            traffic_flow = TrafficFlow.objects.get(id=id)
            traffic_flow_serializer = TrafficFlowWriteSerializer(traffic_flow, data=traffic_flow_data)
            if traffic_flow_serializer.is_valid():
                traffic_flow_serializer.save()
                return Response({"message": "Updated Successfully"})
            return Response(traffic_flow_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except TrafficFlow.DoesNotExist:
            return Response({"message": "TrafficFlow not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, id=0):
        try:
            traffic_flow = TrafficFlow.objects.get(id=id)
            traffic_flow.delete()
            return Response({"message": "Deleted Successfully"})
        except TrafficFlow.DoesNotExist:
            return Response({"message": "TrafficFlow not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#predicition/views.py

import numpy as np
import os 
from tensorflow import keras
class TrafficPredicctionAPI(APIView):
    permission_classes = [IsAuthenticated,IsAdminUser]

    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        model_path = os.path.join('operation', 'models', '2-intersection.keras')
        self.model = keras.models.load_model(model_path)
    def post(self, request):
        # Supongamos que recibimos una lista de secuencias de tiempo
        # Ejemplo: {"data": [[0, 10, 30], [0, 10, 45], [0, 11, 0], [0, 11, 15], [0, 11, 30]]}
        data = request.data.get('data', [])
        
        if not data:
            return JsonResponse({'error': 'No data provided'}, status=400)
        
        # Convertir la entrada a un array de numpy
        input_data = np.array(data)
        input_data = input_data.reshape((1, len(data), 3))  # Asegurarse de que el formato sea el correcto

        # Realizar la predicción
        predicted_traffic_counts = self.model.predict(input_data)

        # Convertir el resultado a una lista para JSON
        predicted_traffic_counts = predicted_traffic_counts.tolist()

        return JsonResponse({'predicted_traffic_counts': predicted_traffic_counts})
    





from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import TrafficFlow, Intersection
from datetime import datetime, timedelta
from django.utils import timezone

def traffic_flow_report(request, intersection_name):
    # Obtener la intersección por nombre
    intersection = get_object_or_404(Intersection, name=intersection_name)
    
    # Obtener la fecha actual con zona horaria
    end_date = timezone.now()
    # Obtener la fecha de hace 7 días con zona horaria
    start_date = end_date - timedelta(days=7)

    # Obtener la zona horaria actual
    current_tz = timezone.get_current_timezone()
    
    # Filtrar registros de TrafficFlow para los últimos 7 días y la intersección específica
    traffic_flows = TrafficFlow.objects.filter(
        timestamp__range=(start_date, end_date),
        laneGroup__intersection=intersection
    )
    
    # Procesar los datos para agruparlos por día y hora
    report_data = {}
    for flow in traffic_flows:
        date_key = flow.timestamp.astimezone(current_tz).strftime('%Y-%m-%d')
        hour_key = flow.timestamp.astimezone(current_tz).strftime('%H:00')
        
        if date_key not in report_data:
            report_data[date_key] = {}
        
        if hour_key not in report_data[date_key]:
            report_data[date_key][hour_key] = []
        
        report_data[date_key][hour_key].append(flow.vehicleCount)
    
    # Agregar lógica para determinar los patrones de tráfico (leve, moderado, saturado)
    for date_key in report_data:
        for hour_key in report_data[date_key]:
            avg_vehicle_count = sum(report_data[date_key][hour_key]) / len(report_data[date_key][hour_key])
            if avg_vehicle_count < 100:
                pattern = 'Leve'
            elif avg_vehicle_count < 150:
                pattern = 'Moderado'
            else:
                pattern = 'Saturado'
            
            report_data[date_key][hour_key] = pattern
    
    return JsonResponse(report_data)


from django.db.models import Avg

def average_vehicle_per_day_report(request):
    # Obtener el promedio de vehículos agrupado por día
    daily_avg = TrafficFlow.objects.extra({'day': "date(timestamp)"}).values('day').annotate(avg_vehicle_count=Avg('vehicleCount')).order_by('day')

    # Crear una lista con los promedios por día
    final_daily_avg = [{'day': entry['day'], 'average': entry['avg_vehicle_count']} for entry in daily_avg]

    response_data = {
        'average_vehicle_per_day': final_daily_avg
    }

    return JsonResponse(response_data)


import random
from django.shortcuts import get_object_or_404
from .traffic_control import calculate_green_time, calculate_red_time

def calculate_pressure_simulated(request, intersection_id):
    try:
        # Obtener los datos de la API de vehículos entrantes y salientes
        intersection = get_object_or_404(Intersection, id=intersection_id)
        lane_groups = LaneGroup.objects.filter(intersection=intersection)
        avenues = Avenue.objects.all()

        total_pressure_by_avenue = {avenue.name: 0 for avenue in avenues}
        pressures = []

        for lane in lane_groups:
            vehicles_in = random.randint(0, lane.capacity)
            vehicles_out = random.randint(0, lane.capacity)
            # Asegurarse de que vehicles_out no sea mayor que vehicles_in
            while vehicles_out > vehicles_in:
                vehicles_out = random.randint(0, lane.capacity)

            max_capacity_in = lane.capacity
            max_capacity_out = lane.capacity

            pressure = (vehicles_in / max_capacity_in) - (vehicles_out / max_capacity_out)


            pressures.append({
                'lane_id': lane.id,
                'direction': lane.direction,
                'vehicles_in': vehicles_in,
                'vehicles_out': vehicles_out,
                'max_capacity_in': max_capacity_in,
                'max_capacity_out': max_capacity_out,
                'pressure': pressure
            })

            avenue_name = lane.avenue.name
            if avenue_name in total_pressure_by_avenue:
                total_pressure_by_avenue[avenue_name] += abs(pressure)

        # Calcular tiempos de verde y rojo en función de la presión
        pressures_sorted = sorted(total_pressure_by_avenue.items(), key=lambda item: item[1], reverse=True)
        green_times = calculate_green_time(pressures_sorted)
        red_times = calculate_red_time(green_times)

        # Actualizar los semáforos en la base de datos
        traffic_lights = TrafficLight.objects.filter(intersection=intersection)
        for light in traffic_lights:
            if light.avenue.name == pressures_sorted[0][0]:  # Mayor presión
                light.greenTime = green_times[0]
                light.redTime = red_times[0]  # Inverso del tiempo rojo
                light.pressure_status="high"
            elif light.avenue.name == pressures_sorted[1][0]:  # Menor presión
                light.greenTime = green_times[1]
                light.redTime = red_times[1]  # Inverso del tiempo verde
                light.pressure_status="low"

            light.save()

        response_data = {
            'intersection_id': intersection.id,
            'intersection_name': intersection.name,
            'total_pressures': total_pressure_by_avenue,
            'pressures': pressures,
            'updated_traffic_lights': [
                {
                    'traffic_light_id': light.id,
                    'avenue_name': light.avenue.name,
                    'green_time': light.greenTime,
                    'red_time': light.redTime
                }
                for light in traffic_lights
            ]
        }
        return JsonResponse(response_data)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    





