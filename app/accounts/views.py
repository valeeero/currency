from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from accounts.models import User


class MyProfileView(UpdateView):
    queryset = User.objects.all()
    fields = (
        'first_name',
        'last_name',
    )
    success_url = reverse_lazy('index')
    template_name = 'my_profile.html'
