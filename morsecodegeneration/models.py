from django.db import models

# Create your models here.


class User(models.Model):
    fname = models.CharField(max_length=40, null=False)
    email = models.EmailField(max_length=30, default='', null=False)
    phoneno = models.CharField(max_length=10, default='', null=False)
    password = models.CharField(max_length=15, default='', null=False)