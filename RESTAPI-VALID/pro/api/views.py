from django.shortcuts import render
from rest_framework import serializers, generics
from .models import Details,Students
from .serializers import DetailsSerializer,StudentsSerializer



#-------------- generics views ---------- students -------------------#
  
class studentsview(generics.ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer

class students(generics.RetrieveUpdateDestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
  
#-------------- generics views ---------- details -------------------# 
  
class viewDetails(generics.ListCreateAPIView):
    queryset = Details.objects.all()
    serializer_class = DetailsSerializer

class details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Details.objects.all()
    serializer_class = DetailsSerializer
