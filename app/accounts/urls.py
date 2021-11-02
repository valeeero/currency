from accounts.views import ActivateUserView, MyProfileView, SingUpView

from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path


app_name = 'accounts'

urlpatterns = [

    path('my_profile/', MyProfileView.as_view(), name='my-profile'),
    path('sign_up/', SingUpView.as_view(), name='sign-up'),
    path('activate/<uuid:username>/', ActivateUserView.as_view(), name='activate-user'),

    url(r'^password_reset/$', auth_views.PasswordResetView.as_view(),
        name='password_reset'),
    url(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'),
    url(r'^reset/done/$',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'),


]
