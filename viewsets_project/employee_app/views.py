from rest_framework import viewsets, status
from .serializers import EmployeeSerializer
from .models import Employee
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    # http_method_names = ['get', 'post', 'patch', 'delete']
    # def get_queryset(self):
    #     return Employee.objects.all()
    
    # def get_serializer_class(self):
    #     return EmployeeSerializer
    
    
    