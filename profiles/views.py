from django.shortcuts import render
from django.http import HttpResponse
def profiles(request):
    return render(request,'profiles.html',{})
