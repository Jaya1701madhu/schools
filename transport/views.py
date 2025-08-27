from django.shortcuts import render

from django.http import HttpResponse

def trans(request):
    #return HttpResponse("<h2>transpot mahhn</h2>")
    return render(request,'transport.html',{})
