from django.urls import path,re_path
from .views import *

urlpatterns = [
    path('register/',register),
    re_path('login/(?P<email>[a-zA-Z0-9]+)/(?P<password>[a-zA-Z0-9]+)/',log_in),
    re_path('logout/(?P<email>[a-zA-Z0-9]+)/(?P<password>[a-zA-Z0-9]+)/',log_out),
    re_path('get_profile/(?P<email>[a-zA-Z0-9]+)/',getProfile),
    re_path('update_profile/(?P<email>[a-zA-Z0-9]+)/',updateProfile),
]
