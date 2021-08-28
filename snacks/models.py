from django.db import models
from django.contrib.auth.models import User


class Snack(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    purchaser = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
