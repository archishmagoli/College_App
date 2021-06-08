from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class JournalEntry(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    emo_choices = (
        ('cry.jpg', 'Terrible'),
        ('sad.jpg', 'Could be better'),
        ('neutral.jpg', 'Alright'),
        ('slight.jpg', 'Good'), 
        ('big.jpg', 'Great')
    )
    mood = models.CharField(max_length=30, blank=True, null=True, choices=emo_choices)
    journal = models.TextField(max_length=500)

    def __str__(self):
        return self.title