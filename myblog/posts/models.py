from django.db import models

class News(models.Model):
    title = models.CharField(max_length=40, blank=False)
    description = models.CharField(max_length=100, blank=False)
    text = models.TextField(max_length=500, blank=False)
    date = models.DateField(default="2024-12-15")

    def __str__(self):
        return f'{self.title} - {self.date}'


STATUS_CHOICES = {
    "d": "Draft",
    "p": "Published",
    "w": "Withdrawn",
}

class Comment(models.Model):
    name = models.CharField(max_length=40, blank=False)
    email = models.EmailField(blank=False)
    text = models.TextField(max_length=500, blank=False)
    new = models.ForeignKey(News, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="d")

    def __str__(self):
        return f'{self.name} - {self.email} - {self.status}'
