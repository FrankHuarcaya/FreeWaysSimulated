# Generated by Django 5.0.6 on 2024-05-24 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0005_rename_length_meters_avenue_lengthmeters_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intersection',
            name='location',
            field=models.CharField(max_length=255, null=True),
        ),
    ]