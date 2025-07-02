from django.contrib import admin

from.models import Doctors,Patient,Prescription,Payment

admin.site.register(Doctors)
admin.site.register(Patient)
admin.site.register(Prescription)
admin.site.register(Payment)