from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=25)
    email = models.EmailField(max_length=250)
    description = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name