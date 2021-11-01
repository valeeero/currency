from currency.views import (
    ContactUsCreateView, RateCreateView, RateDeleteView,
    RateDetailView, RateListView, RateUpdateView,
    SourceCreateView, SourceDeleteView, SourceDetailView,
    SourceListView, SourceUpdateView, contactus,
    generate_password, hello_world
)

from django.urls import path

app_name = 'currency'

urlpatterns = [

    path('', hello_world, name='index'),

    path('rate/list/', RateListView.as_view(), name='rate-list'),
    path('rate/create/', RateCreateView.as_view(), name='rate-create'),
    path('rate/details/<int:pk>/', RateDetailView.as_view(), name='rate-details'),
    path('rate/update/<int:pk>/', RateUpdateView.as_view(), name='rate-update'),
    path('rate/delete/<int:pk>/', RateDeleteView.as_view(), name='rate-delete'),

    path('source/', SourceListView.as_view(), name='source-list'),
    path('source/create/', SourceCreateView.as_view(), name='source-create'),
    path('source/details/<int:pk>/', SourceDetailView.as_view(), name='source-details'),
    path('source/update/<int:pk>/', SourceUpdateView.as_view(), name='source-update'),
    path('source/delete/<int:pk>/', SourceDeleteView.as_view(), name='source-delete'),

    path('contactus/create/', ContactUsCreateView.as_view(), name='contactus-create'),

    path('gen-pass/', generate_password),
    path('contact/', contactus, name='contactus'),
]
