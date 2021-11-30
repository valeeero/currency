from currency import model_choises as mch

from django.db import models


def upload_logo(instance, filename):
    return f'logo/{instance.id}/{filename}'


class Source(models.Model):
    source_url = models.URLField(max_length=255)
    name = models.CharField(max_length=64)
    code_name = models.CharField(max_length=24, unique=True, editable=False)
    logo = models.FileField(
        upload_to=upload_logo,
        blank=True,
        null=True,
        default=None,
    )


class Rate(models.Model):
    sale = models.DecimalField(max_digits=5, decimal_places=2)
    buy = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    type = models.CharField(  # noqa

        max_length=3,
        choices=mch.RATE_TYPES,
        blank=False,
        null=False,
        default=mch.TYPE_USD,
    )


class ContactUs(models.Model):
    email_from = models.EmailField(max_length=254)
    subject = models.CharField(max_length=16)
    message = models.TextField(max_length=255)


class ResponseLog(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    status_code = models.PositiveSmallIntegerField()
    path = models.CharField(max_length=255)
    response_time = models.PositiveSmallIntegerField(
        help_text='in milliseconds.'
    )
    request_method = models.CharField(max_length=4, choices=mch.METHODS)
