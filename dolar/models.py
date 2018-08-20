from django.db import models

# Create your models here.

class Dolar(models.Model):
    value = models.DecimalField(max_digits = 7, decimal_places = 3 )
    date = models.DateField( primary_key=True , unique=True)

    def __str__(self):
        return self.value
