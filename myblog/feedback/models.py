from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=40, blank=False)
    email = models.EmailField(blank=False)
    text = models.TextField(max_length=500, blank=False)


    def __str__(self):
        return f'{self.name} - {self.email}'


