from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Student


class StidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id','name', 'age', 'description')

class StidentMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id','name')
