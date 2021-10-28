import debug_toolbar

from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),

    path('', TemplateView.as_view(template_name='home.html'), name='index'),

    path('currency/', include('currency.urls')),
    path('accounts/', include('accounts.urls')),

    url(r'^admin/', admin.site.urls),
    url(r'^silk/', include('silk.urls', namespace='silk')),

]
