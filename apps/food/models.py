from django.db import models

class Food(models.Model):
    name = models.TextField(max_length=200)
    color = models.TextField(max_length=200)

    def __str__(self):
        return self.name

