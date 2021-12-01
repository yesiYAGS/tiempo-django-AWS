from django.shortcuts import render, redirect,HttpResponse
from time import strftime, localtime
# Create your views here.

def hola(request):
    return HttpResponse('funciona') 

def index(request):
    context = {
        "time": strftime("%b %d,%Y %X ", localtime())
    }
    return render(request,'tiempo.html', context)



