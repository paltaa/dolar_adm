from django.db import models

# Create your models here.

class Dolar(models.Model):
    value = models.DecimalField(max_digits = 7, decimal_places = 3 )
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.value
