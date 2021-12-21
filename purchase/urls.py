from django.urls import path
from .views import *

#purchase/
urlpatterns = [
    path('put_buy_req/<int:pid>/', putBuyReq),
    path('delete_buy_req/<int:pid>/', deleteBuyReq),
    path('get_all_buy_req/', getAllBuyReq),
]
