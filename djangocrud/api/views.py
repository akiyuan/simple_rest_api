from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from api.serializers import StidentSerializer,StidentMiniSerializer
from .models import Student
from rest_framework.response import Response


class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Student.objects.all()
    serializer_class = StidentSerializer

    def list(self,request,*args,**kwargd):
        students = Student.objects.all()
        serializer = StidentMiniSerializer(students,many = True)
        return Response(serializer.data)
