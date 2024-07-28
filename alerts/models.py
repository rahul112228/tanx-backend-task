from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField 

class Alert(models.Model):
    STATUS_CHOICES = [
        ('created', 'Created'),
        ('deleted', 'Deleted'),
        ('triggered', 'Triggered'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cryptocurrency = models.CharField(max_length=50) 
    target_price = models.DecimalField(max_digits=15, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='created')
    
    def __str__(self):
        return f'{self.user} - {self.cryptocurrency} at ${self.target_price}'