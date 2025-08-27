from django.shortcuts import render
from django.http import HttpResponse
from admissions.models import Admission

def home(request):
    #return HttpResponse("<H1>hello this is sample class</H1>")
    #return render(request,'index.html',{})
    data=Admission.objects.all()
    res=render(request,'index.html',{'data':data})
    return res
def products(request):
    #return HttpResponse("<h1>productionss is here</h2>")
    return render(request,'products.html',{})
def services(request):
    #return HttpResponse("<>this is services page</>")
    return render(request,'services.html',{})

def login(request):
    return render(request,'login.html',{})