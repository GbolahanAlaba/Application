from django.db import models

class signup(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    repassword = models.CharField(max_length=100)

# Create your models here.
