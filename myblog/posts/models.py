from django.db import models

class Posts(models.Model):
    title = models.CharField(max_length=40, blank=False)
    description = models.CharField(max_length=100, blank=False)
    text = models.TextField(max_length=500, blank=False)
    date = models.DateField(default="2024-12-15")

