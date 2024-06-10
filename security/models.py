# security/models.py
from django.contrib.auth.models import User
from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Añadir el campo role directamente al modelo User
User.add_to_class('role', models.ForeignKey(Role, on_delete=models.CASCADE, null=True))
