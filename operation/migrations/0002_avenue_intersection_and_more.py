# Generated by Django 5.0.6 on 2024-05-23 10:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avenue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Intersection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameField(
            model_name='trafficlight',
            old_name='Latitude',
            new_name='latitude',
        ),
        migrations.AddField(
            model_name='trafficlight',
            name='yellow_time',
            field=models.FloatField(default=3),
        ),
        migrations.AddField(
            model_name='trafficlight',
            name='intersection',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='operation.intersection'),
        ),
        migrations.CreateModel(
            name='LaneGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direction', models.CharField(max_length=50)),
                ('capacity', models.IntegerField()),
                ('num_lanes', models.IntegerField()),
                ('avenue', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='operation.avenue')),
                ('intersection', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='operation.intersection')),
            ],
        ),
        migrations.AddField(
            model_name='trafficlight',
            name='lane_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='operation.lanegroup'),
        ),
    ]
