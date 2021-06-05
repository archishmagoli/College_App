from django.db import models

# Create your models here.
class College(models.Model):
    name = models.CharField(max_length=200)
    college_choice = (
        ('Safety', 'Safety'),
        ('Match', 'Match'),
        ('Reach', 'Reach'),
    )
    category = models.CharField(max_length=30, blank=True, null=True, choices=college_choice)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name