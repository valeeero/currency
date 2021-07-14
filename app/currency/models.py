from django.db import models

class Rate(models.Model):
    sale = models.DecimalField(max_digits=5, decimal_places=2)
    buy = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=32) # examples: privatbank, monobank
    type = models.CharField(max_length=3) # examples: USD, EUR