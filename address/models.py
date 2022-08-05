from django.db import models

# Create your models here.
class Address(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=15)
    emp_code = models.CharField(max_length=20, default=0)