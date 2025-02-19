from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Users(AbstractUser):
	USER_TYPE_CHOICES = [
        ('Doctor', 'Doctor'),
        ('Patient', 'Patient'),
    ]     
	address = models.TextField()
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	pincode = models.CharField(max_length=10)
	usertype = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
	
	# name = models.CharField(max_length=100)
	# email = models.EmailField(unique=True)
	# username = models.CharField(max_length=50, unique=True)
	# password = models.CharField(max_length=100)

	def __str__(self):
		return f"{self.first_name} ({self.usertype})"