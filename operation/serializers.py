from rest_framework import serializers
from .models import Avenue, Intersection, LaneGroup, TrafficLight,TrafficFlow


class IntersectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intersection
        fields = '__all__'

class AvenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avenue
        fields = '__all__'


class LaneGroupWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaneGroup
        fields = '__all__'

class LaneGroupReadSerializer(serializers.ModelSerializer):
    avenue = AvenueSerializer()  # Cambia esto para usar AvenueReadSerializer
    intersection = IntersectionSerializer()  # Cambia esto para usar AvenueReadSerializer
    class Meta:
        model = LaneGroup
        fields = '__all__'

class TrafficLightWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrafficLight
        fields = '__all__'

class TrafficLightReadSerializer(serializers.ModelSerializer):
    intersection = IntersectionSerializer()  # Cambia esto para usar AvenueReadSerializer
    avenue = AvenueSerializer()  # Cambia esto para usar AvenueReadSerializer
    class Meta:
        model = TrafficLight
        fields = '__all__'


class TrafficFlowWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrafficFlow
        fields = '__all__'

class TrafficFlowReadSerializer(serializers.ModelSerializer):
    laneGroup = LaneGroupReadSerializer()
    class Meta:
        model = TrafficFlow
        fields = '__all__'