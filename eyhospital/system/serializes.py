from rest_framework import serializers
from .models import Doctors,Patient,Prescription,Payment
from django.contrib.auth.models import User

class DoctorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = '__all__'

class PatientSeializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
        

class UserSerializer(serializers.ModelSerializer):
    
    password=serializers.CharField(write_only=True)    
    class Meta:
        model = User
        fields = ['username','password','email']
        
    def create(self,validated_data):
        user = User.objects.create_user(username=validated_data["username"], 
                                  password=validated_data["password"],
                                  email=validated_data.get("email",''))
        return user