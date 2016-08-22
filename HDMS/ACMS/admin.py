from django.contrib import admin
from .models import hmo_list, patient, drug
# Register your models here.
admin.site.register(hmo_list)
admin.site.register(patient)
admin.site.register(drug)
