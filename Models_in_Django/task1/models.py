from django.db import models


# Create your models here.


class Buyer(models.Model):
    name = models.CharField(max_length=15, verbose_name='username')
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.DecimalField(max_digits=20, decimal_places=4)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='Game')


    def __str__(self):
        return self.title



