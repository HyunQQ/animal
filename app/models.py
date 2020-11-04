from django.db import models

class AnimalUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    interest = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
