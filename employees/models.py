from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    number = models.IntegerField()
    position = models.CharField(max_length=200)
    resume = models.FileField(blank=True, null=True, upload_to='files/')