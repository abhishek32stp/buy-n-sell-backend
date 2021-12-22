from django.db import connection
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import *
from .models import *

def serialize(cols,rows):
    l=[]
    for row in rows:
        d=dict([(x,y) for x,y in zip(cols,row)])
        l.append(d)
    return l

# Create your views here.
def login(request,email,password):
    print(email)
    print(password)

    obj=CustomUser.objects.create(email=email,password=password,phone_no="+8424432398")

    return HttpResponse('Bhag bsdk')


def getProfile(request,email):
    get_pf_fields=["email","phone_no"]
    query="select ";
    for i in get_pf_fields:
        query+=" "+i+" "
        if(i!=get_pf_fields[-1]) : query+=","
    query+=" from user_customuser where email='"+str(email)+"'"
    print(query)

    cursor=connection.cursor()
    cursor.execute(query)
    rows=cursor.fetchall()
    objs=serialize([dec[0] for dec in cursor.description],rows)

    return JsonResponse(objs,safe=False)