from django.contrib.auth.models import User
from django.db import models


class Doctor(models.Model):
    user = models.OneToOneField(User)
    address = models.CharField(max_length=255, default="")
    city = models.CharField(max_length=200, default="")
    phone_number = models.CharField(max_length=20, default=0)


class Patient(models.Model):
    name = models.CharField(max_length=200, default="")
    address = models.CharField(max_length=255, default="")
    city = models.CharField(max_length=200, default="")
    phone_number = models.CharField(max_length=20, default=0)

