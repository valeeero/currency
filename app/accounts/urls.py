from accounts.views import MyProfileView

from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path


app_name = 'accounts'

urlpatterns = [

    path('my_profile/', MyProfileView.as_view(), name='my-profile'),

    url(r'^password_reset/$', auth_views.PasswordResetView.as_view(
            template_name='reset_pass/password_reset_form.html',
            email_template_name='reset_pass/password_reset_email.html',
            subject_template_name='reset_pass/password_reset_subject.txt',
            ), name='password_reset'),
    url(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(
        template_name='reset_pass/password_reset_done.html'),
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='reset_pass/password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^reset/done/$',
        auth_views.PasswordResetCompleteView.as_view(template_name='reset_pass/password_reset_complete.html'),
        name='password_reset_complete'),
]
