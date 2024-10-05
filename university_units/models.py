from django.db import models

class Office(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    location = models.CharField(max_length=500)
    manager = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name
    

