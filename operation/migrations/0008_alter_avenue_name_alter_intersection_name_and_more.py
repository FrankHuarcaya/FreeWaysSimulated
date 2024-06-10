# Generated by Django 5.0.6 on 2024-05-24 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0007_remove_intersection_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avenue',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='intersection',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='lanegroup',
            name='capacity',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='lanegroup',
            name='direction',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lanegroup',
            name='numLanes',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='trafficlight',
            name='brand',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='trafficlight',
            name='latitude',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='trafficlight',
            name='longitude',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='trafficlight',
            name='redGreen',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='trafficlight',
            name='redTime',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='trafficlight',
            name='status',
            field=models.CharField(max_length=255, null=True),
        ),
    ]