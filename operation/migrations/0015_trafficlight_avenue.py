# Generated by Django 5.0.6 on 2024-05-26 09:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0014_rename_redgreen_trafficlight_greentime'),
    ]

    operations = [
        migrations.AddField(
            model_name='trafficlight',
            name='avenue',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='operation.avenue'),
        ),
    ]