from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=256)
    uid = models.CharField(max_length=16)
    
    
