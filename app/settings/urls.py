from currency.views import contactas, generate_password, hello_world, rate_list

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', hello_world),
    path('gen-pass/', generate_password),
    path('rate/list/', rate_list),
    path('contact/', contactas),
]
