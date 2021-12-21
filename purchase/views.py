from django.shortcuts import render
from django.http import *
from django.db import *
from .models import *
import random


def serialize(cols,rows):
    l=[]
    for row in rows:
        d=dict([(x,y) for x,y in zip(cols,row)])
        l.append(d)
    return l


def getUid(request):
    return random.randint(0,10)


def putBuyReq(request,pid):
    #if(request.method!="POST") : return HttpResponse(request.method+"  request not allowed")
    user=getUid(request)
    try:
        obj=PurchaseReq(buy_user=user,pid=pid)
        obj.save()
    except Exception as e:
        print(e)
        return HttpResponse("Some Error Occured")

    return HttpResponse("Buy Req Added")


def deleteBuyReq(request,pid):
    user=getUid(request)
    try:
        obj=PurchaseReq.objects.get(buy_user=user,pid=pid)
        obj.delete()
    except Exception as e:
        print(e)
        return HttpResponse("Some Error Occured")

    return HttpResponse("Buy Req Removed")



def getAllBuyReq(request):
    user=getUid(request)
    cursor=connection.cursor()
    cursor.execute("select * from purchase_purchasereq where buy_user="+str(user))
    rows=cursor.fetchall()
    objs=serialize([dec[0] for dec in cursor.description],rows)
    return JsonResponse(objs,safe=False)
    


def getAllBuyProd(request):
    user=getUid(request)
    cursor=connection.cursor()
    cursor.execute("select * from purchase_purchasereq p_req,product_product prod "+
                    "where p_req.buy_user="+str(user)+" and p_req.pid=prod.key")
    rows=cursor.fetchall()
    objs=serialize([dec[0] for dec in cursor.description],rows)
    return JsonResponse(objs,safe=False)