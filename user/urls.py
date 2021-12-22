from django.urls import path,re_path
from .views import *

urlpatterns = [
    re_path('login/(?P<email>[a-zA-Z0-9]+)/(?P<password>[a-zA-Z0-9]+)/',login),
    re_path('get_profile/(?P<email>[a-zA-Z0-9]+)/',getProfile),
]
