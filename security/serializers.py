# security/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Role

class UserSerializer(serializers.ModelSerializer):
    role = serializers.SlugRelatedField(slug_field='name', queryset=Role.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name', 'role','is_active']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        role_data = validated_data.pop('role')
        user = User.objects.create(**validated_data)
        user.role = role_data
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, instance, validated_data):
        role_data = validated_data.pop('role')
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.is_active = validated_data.get('is_active', instance.is_active)

        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)

        instance.role = role_data
        instance.save()
        return instance
