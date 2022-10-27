from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# tylko custom user
# zadaliśmy te pola aby były obowiązkoewe do podania w formularzu
# blank = Flase
class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(unique=True) # unique
    phone_number = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=6)
    town_name = models.CharField(max_length=32)
