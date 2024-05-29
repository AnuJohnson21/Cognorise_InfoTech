from django.db import models
# Create your models here.

class bmi(models.Model):
    age=models.IntegerField()
    gender=models.CharField(max_length=20)
    height=models.IntegerField()
    weight=models.IntegerField()
    result=models.IntegerField()
