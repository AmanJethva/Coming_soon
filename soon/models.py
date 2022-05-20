import email
from django.db import models

# Create your models here.

class Index(models.Model):
    email=models.CharField(max_length=122, default=0)