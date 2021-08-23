from django.db import models
import string


class Rate(models.Model):
    sale = models.DecimalField(max_digits=5, decimal_places=2)
    buy = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=32)  # examples: privatbank, monobank
    type = models.CharField(max_length=3)  # noqa


class ContactUs(models.Model):
    email_from = models.EmailField(max_length=254)
    subject = models.CharField(max_length=16)
    message = models.TextField(max_length=255)


class Source(models.Model):
    source_url = models.URLField(max_length=255)
    name = models.CharField(max_length=64)
