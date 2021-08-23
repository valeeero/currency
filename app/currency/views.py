from django.shortcuts import render  # noqa

from currency.models import ContactUs, Rate # noqa
from currency.utils import generate_password as gen_pass

from django.http import HttpResponse


# Create your views here.


def hello_world(request):
    return render(request, 'home.html')


def generate_password(request):
    password_len = int(request.GET.get('password-len'))
    password = gen_pass(password_len)
    return HttpResponse(password)


def rate_list(request):
    rates = Rate.objects.all()
    context = {
        'rate_list': rates,
    }
    return render(request, 'rate_list.html', context=context)


def contactas(request):
    contacts = ContactUs.objects.all()
    context = {
        'contact': contacts
    }
    return render(request, 'contact.html', context=context)


def response_code(request):
    response = HttpResponse('Status Code', status=200)
    return response
