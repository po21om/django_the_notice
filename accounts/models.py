from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True)
    postal_code = models.CharField(max_length=6, blank=True)
    town_name = models.CharField(max_length=32, blank=True)
