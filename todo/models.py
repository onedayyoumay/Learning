from django.db import models
# Create your models here.
class tasks(models.Model):
    status = models.BooleanField()
    task = models.CharField(max_length=100)