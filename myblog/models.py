from django.db import models


class register(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=255)
    password = models.IntegerField(max_length=20)

# Create your models here.
