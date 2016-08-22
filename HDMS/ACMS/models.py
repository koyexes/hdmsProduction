from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class hmo_list(models.Model):
    name = models.CharField(max_length = 200)
    mobile = models.CharField(max_length = 100, null = True, blank = True)
    email = models.EmailField(help_text = "Please enter a valid email address!", default = "no email")
    address = models.TextField(default = 'no address')
    hmo_status = models.BooleanField('Hmo Status', help_text = 'uncheck if HMO is not active', default = '0')

    def __str__(self):
        return self.name

class patient(models.Model):
    surname = models.CharField(max_length = 20)
    firstname = models.CharField(max_length = 20)
    card_no = models.CharField(max_length = 15)
    gender = models.CharField(max_length = 1, choices=(("M", "Male"), ("F", "Female")), default="M");
    phone_number = models.CharField(max_length = 15)
    address = models.CharField(max_length = 50)
    hmo_id = models.ForeignKey(hmo_list,verbose_name="hmo_id", default= 0)
    date_added = models.DateTimeField(default=timezone.now)
    added_by = models.ForeignKey(User, default=0)

    def __str__(self):
        return ("%s %s" % (self.surname, self.firstname)).upper()

class drug(models.Model):
    drug_name = models.CharField(max_length=50)
    drug_code = models.CharField(max_length=15)
    date_added = models.DateTimeField(default=timezone.now)
    added_by = models.ForeignKey(User, default=0)

