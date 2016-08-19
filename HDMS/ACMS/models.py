from __future__ import unicode_literals

from django.db import models

# Create your models here.
class hmo_list(models.Model):
    name = models.CharField(max_length = 200)
    mobile = models.CharField(max_length = 20, null = True, blank = True)
    email = models.EmailField(help_text = "Please enter a valid email address!", default = "no email")
    address = models.TextField(default = 'no address')
    hmo_status = models.BooleanField('Hmo Status', help_text = 'uncheck if HMO is not active', default = '0')

    def __str__(self):
        return self.name
