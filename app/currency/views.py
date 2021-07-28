from django.shortcuts import render  # noqa

from currency.models import ContactUs, Rate # noqa
from currency.utils import generate_password as gen_pass

from django.http import HttpResponse


# Create your views here.


def hello_world(request):
    return HttpResponse('Hello world')


def generate_password(request):
    password_len = int(request.GET.get('password-len'))
    password = gen_pass(password_len)
    return HttpResponse(password)


def rate_list(request):
    rates = Rate.objects.all()
    result = []
    for rate in rates:
        # breakpoint()
        result.append(
            f'ID: {rate.id} Sale: {rate.sale} Buy: {rate.buy}</br>'
            f'ID: {rate}</br>'
        )
    return HttpResponse(str(result))


def contactas(request):
    contacts = ContactUs.objects.all()
    result = []
    for contact in contacts:
        # breakpoint()
        result.append(
            f'contact: {contact}'
        )
    return HttpResponse(str(result))
