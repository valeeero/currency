from currency.views import (
    ContactUsCreateView, RateCreateView, RateDeleteView,
    RateDetailView, RateListView, RateUpdateView,
    SourceCreateView, SourceDeleteView, SourceDetailView,
    SourceListView, SourceUpdateView, contactus,
    generate_password, hello_world
)

import debug_toolbar

from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),

# __debug__/
# admin/
# auth/ login/ [name='login']
# auth/ logout/ [name='logout']
# auth/ password_change/ [name='password_change']
# auth/ password_change/done/ [name='password_change_done']
# auth/ password_reset/ [name='password_reset']
# auth/ password_reset/done/ [name='password_reset_done']
# auth/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
# auth/ reset/done/ [name='password_reset_complete']


    path('', hello_world, name='index'),
    path('gen-pass/', generate_password),
    path('contact/', contactus, name='contactus'),

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

    path('contactus/create/', ContactUsCreateView.as_view(), name='contactus-create'),
    url(r'^admin/', admin.site.urls),
    url(r'^silk/', include('silk.urls', namespace='silk')),

]
