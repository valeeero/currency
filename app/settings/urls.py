from currency.views import (
    contactas, generate_password,
    hello_world, rate_list, rate_create,
    rate_details, rate_update, rate_delete, source_create,
    sources, source_update, source_details, source_delete
)

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', hello_world),
    path('gen-pass/', generate_password),
    path('rate/list/', rate_list),
    path('contact/', contactas),
    path('rate/create/', rate_create),
    path('rate/details/<int:rate_id>/', rate_details),
    path('rate/update/<int:rate_id>/', rate_update),
    path('rate/delete/<int:rate_id>/', rate_delete),
    path('source/', sources),
    path('source/create/', source_create),
    path('source/update/<int:source_id>/', source_update),
    path('source/details/<int:source_id>/', source_details),
    path('source/delete/<int:source_id>/', source_delete),

]
