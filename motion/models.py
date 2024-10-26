from django.db import models

# Create your models here.
class Motion(models.Model):
    marca = models.CharField(max_length=200)
    sucursal = models.CharField(max_length=200)
    aspirante = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

