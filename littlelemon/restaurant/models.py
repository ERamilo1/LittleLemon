from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    guests = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    date = models.DateField()

    def __str__(self):
        return self.name

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])