# from django.shortcuts import render
from rest_framework import generics
from .models import Doctors
from .serializes import DoctorsSerializer,UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

class DoctorsList (generics.ListCreateAPIView):
    queryset = Doctors.objects.all()
    serializer_class = DoctorsSerializer
    
class DotorsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctors.objects.all()
    serializer_class = DoctorsSerializer
    permission_classes = [IsAuthenticated]
     
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []