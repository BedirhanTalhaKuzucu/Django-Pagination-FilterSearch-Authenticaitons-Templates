from django.db import models
from django.db.models.fields import BooleanField
from django.contrib.auth.models import User

# Create your models here.

class  Todo(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=50)
    description = models.TextField()
    TITLE = (
        ("H", "High"),
        ("M", "Medium"),
        ("L", "Low"),
    )
    
    priority = models.CharField(max_length=50, choices=TITLE, default="L")
    done = models.BooleanField()
    updateDate = models.DateTimeField(auto_now=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.task
    
    
