# Generated by Django 5.0.6 on 2024-06-03 01:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0016_trafficlight_pressure_status_trafficflow'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trafficflow',
            old_name='lane_group',
            new_name='laneGroup',
        ),
        migrations.RenameField(
            model_name='trafficflow',
            old_name='vehicle_count',
            new_name='vehicleCount',
        ),
    ]