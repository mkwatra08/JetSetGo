from django.db import models

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=120, default='')
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=120, default='')
    message = models.TextField()
    date = models.DateField()
    
    def __str__(self):
        return self.name    