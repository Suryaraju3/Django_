# from django.shortcuts import render
from rest_framework import generics
from .models import Doctors,Patient,Prescription,Payment
from .serializes import DoctorsSerializer,UserSerializer,PatientSeializer,PrescriptionSerializer,PaymentSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

class DoctorsList (generics.ListCreateAPIView):
    queryset = Doctors.objects.all()
    serializer_class = DoctorsSerializer
    
class PatientList(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSeializer

class PerscriptionList(generics.ListCreateAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    
class PaymentList(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = Payment
    
    
class DotorsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctors.objects.all()
    serializer_class = DoctorsSerializer
    permission_classes = [IsAuthenticated]
     
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []