from django.db import models

class Doctors(models.Model):
    Name=models.CharField(max_length=100)
    diseasesName=models.CharField(max_length=200)
    
    def __str__(self):
        return self.Name
    
    

