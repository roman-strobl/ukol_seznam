from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=100)
    shortName = models.CharField(max_length=50, null=True)
    iconUri = models.CharField(max_length=200)
    manifestUri = models.CharField(max_length=200)
    description = models.TextField(max_length=255, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Features(models.Model):
    name = models.CharField(max_length=50)
    movies = models.ManyToManyField(Movie)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name}: {self.movies}"