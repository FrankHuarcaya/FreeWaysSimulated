# Generated by Django 5.0.6 on 2024-05-24 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0008_alter_avenue_name_alter_intersection_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lanegroup',
            old_name='intersection',
            new_name='intersectionId',
        ),
    ]