from django.db import models

# Create your models here.

    
class Intersection(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,null=True)
    latitude =models.CharField(max_length=255,null=True)
    longitude =models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.name
    
    
class Avenue(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,null=True)
    description = models.TextField(null=True, blank=True)
    lengthMeters = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name
    

class LaneGroup(models.Model):
    id=models.AutoField(primary_key=True)
    avenue = models.ForeignKey(Avenue, on_delete=models.CASCADE,null=True)
    direction = models.CharField(max_length=50,null=True)
    capacity = models.IntegerField(null=True)
    numLanes = models.IntegerField(null=True)
    intersection = models.ForeignKey(Intersection, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f"{self.direction} on {self.avenue.name} with {self.num_lanes} lanes"
    


class TrafficLight(models.Model):
    id=models.AutoField(primary_key=True)
    intersection = models.ForeignKey(Intersection, on_delete=models.CASCADE,null=True)
    avenue = models.ForeignKey(Avenue, on_delete=models.CASCADE,null=True)
    status=models.CharField(max_length=255,null=True)
    latitude =models.CharField(max_length=255,null=True)
    longitude =models.CharField(max_length=255,null=True)
    brand=models.CharField(max_length=255,null=True)
    redTime=models.IntegerField(null=True)
    greenTime=models.IntegerField(null=True)
    yellowTime = models.FloatField(default=3)
    pressure_status = models.CharField(max_length=50, null=True)  # Nuevo campo para la presión


    
    def __str__(self):
        return f"Traffic Light {self.id} at {self.intersection.name}"


class TrafficFlow(models.Model):
    laneGroup = models.ForeignKey(LaneGroup, on_delete=models.CASCADE,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    vehicleCount = models.IntegerField()

    def __str__(self):
        return f'{self.intersection} - {self.lane_group} - {self.timestamp} - {self.vehicle_count}'