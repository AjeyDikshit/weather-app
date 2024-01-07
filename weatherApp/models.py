from django.db import models

class Citie(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):  # show the actual city name on the dashboard
        return self.name

