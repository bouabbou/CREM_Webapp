from django.db import models
from django.utils import timezone
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.name} - {self.email} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"