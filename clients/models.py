from django.db import models

# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    number = models.IntegerField()
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=700)