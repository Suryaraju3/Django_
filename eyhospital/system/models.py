from django.db import models

class Doctors(models.Model):
    Name=models.CharField(max_length=100)
    diseasesName=models.CharField(max_length=200)
    
    def __str__(self):
        return self.Name
    

class Patient(models.Model):
    Pid=models.AutoField(primary_key=True)
    pname=models.CharField(max_length=100)
    age=models.IntegerField()
    gender=models.CharField(max_length=6)
    visiteddate=models.DateTimeField(auto_now=True)
    Did=models.ForeignKey(Doctors, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.pname 
    
class Prescription(models.Model):
    Prescriptionid=models.AutoField(primary_key=True)
    pid=models.ForeignKey(Patient, on_delete=models.CASCADE)
    presdate=models.DateField(auto_now=True)
    medicine=models.TextField()
    
    def __str__(self):
        return self.medicine 

class Payment(models.Model):
    id=models.AutoField(primary_key=True)
    Prescriptionid=models.ForeignKey(Prescription, on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.amount
    

