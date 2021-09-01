from currency.views import (
    RateCreateView, RateDeleteView, RateDetailView,
    RateListView, RateUpdateView, SourceCreateView,
    SourceDeleteView, SourceDetailView, SourceListView,
    SourceUpdateView, contactas, generate_password, hello_world
)

import debug_toolbar

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),

    path('', hello_world),
    path('gen-pass/', generate_password),
    path('contact/', contactas),

    path('currency/rate/list/', RateListView.as_view(), name='rate-list'),
    path('currency/rate/create/', RateCreateView.as_view(), name='rate-create'),
    path('currency/rate/details/<int:pk>/', RateDetailView.as_view(), name='rate-details'),
    path('currency/rate/update/<int:pk>/', RateUpdateView.as_view(), name='rate-update'),
    path('currency/rate/delete/<int:pk>/', RateDeleteView.as_view(), name='rate-delete'),

    path('source/', SourceListView.as_view(), name='source-list'),
    path('source/create/', SourceCreateView.as_view(), name='source-create'),
    path('source/details/<int:pk>/', SourceDetailView.as_view(), name='source-details'),
    path('source/update/<int:pk>/', SourceUpdateView.as_view(), name='source-update'),
    path('source/delete/<int:pk>/', SourceDeleteView.as_view(), name='source-delete'),

]
