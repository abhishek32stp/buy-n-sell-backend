from django import http
from django.db import connection
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import *
from django.contrib.auth import authenticate,login,logout

from .models import *

def serialize(cols,rows):
    l=[]
    for row in rows:
        d=dict([(x,y) for x,y in zip(cols,row)])
        l.append(d)
    return l


def register(request):
    email=request.POST.get('email')
    password=request.POST.get('password')
    phone_no=request.POST.get('phone_no')
    image=request.FILES.get('image')

    print(email)
    print(password)

    obj=CustomUser(email=email,password=password,phone_no=phone_no)
    obj.is_active=False
    obj.image=image
    obj.save()

    return HttpResponse('Kar Diya Register')



def log_in(request,email,password):
    if request.user.is_authenticated: return HttpResponse("Sale Chutiya Hai Kya, Dobara Login Kar Raha H")
    print(email)
    print(password)

    try:
        user=CustomUser.objects.get(email=email,password=password)
    except Exception as e:
        return HttpResponse("Sahi Details Daal, Aise Nahi Chalega")

    login(request, user)
    return HttpResponse("User Authnticated")


def log_out(request,email,password):
    if not request.user.is_authenticated: return HttpResponse("Pahle Login Kar Le")
    logout(request)



def getProfile(request,email):
    get_pf_fields=["email","phone_no"]
    try:
        obj=CustomUser.objects.get(email=email)
    except Exception as e:
        return HttpResponse("Register Kar Pahle")

    d=obj.__dict__
    r={}
    for att in get_pf_fields:
        r[att]=d.get(att,None)

    return JsonResponse(r,safe=False)



def updateProfile(request,email):
    pass



# def getProfile(request,email):
#     get_pf_fields=["email","phone_no"]
#     query="select ";
#     for i in get_pf_fields:
#         query+=" "+i+" "
#         if(i!=get_pf_fields[-1]) : query+=","
#     query+=" from user_customuser where email=%s"
#     print(query)
#     cursor=connection.cursor()
#     cursor.execute(query,[str(email)])
#     rows=cursor.fetchall()
#     if len(rows)<=0: return HttpResponse("User Not Exists")
#     objs=serialize([dec[0] for dec in cursor.description],rows)

#     return JsonResponse(objs,safe=False)