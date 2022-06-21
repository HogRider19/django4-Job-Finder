from pyexpat import model
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    reviews = models.FloatField(blank=True)

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    reviews = models.FloatField()
    company = models.ManyToManyField(Company)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    lowerPrice = models.FloatField(blank=True)
    upperPrice = models.FloatField(blank=True)
    volute = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Profession(models.Model):
    name = models.CharField(max_length=100)
    vacancy = models.ManyToManyField(Vacancy)

    def __str__(self):
        return self.name


