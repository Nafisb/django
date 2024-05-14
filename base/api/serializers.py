from rest_framework import serializers
from django.contrib.auth.models import User
from base.models import Network


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']
        #extra_kwargs = {'password': {'write_only': True}}


class NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Network
        fields = '__all__'
