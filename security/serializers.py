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
    

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Agregar información personalizada al payload
        token['role'] = user.role.name  # Asumiendo que el modelo User tiene un atributo 'role'
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        # Agregar el rol al objeto de respuesta
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['role'] = self.user.role.name  # Envía el rol junto con los tokens
        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
