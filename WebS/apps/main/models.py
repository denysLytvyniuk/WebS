from django.db import models


class Price(models.Model):
    currency = models.CharField(max_length=50, unique=True)
    symbol = models.CharField(max_length=10, unique=True)
    price = models.DecimalField(max_digits=20, decimal_places=10)

    def __str__(self):
        return self.currency


