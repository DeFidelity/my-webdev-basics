from django.db import models

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=50, unique=True)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=60)

    def __str__(self):
        return self.first_name
''' username apptwo
password secondapp'''
