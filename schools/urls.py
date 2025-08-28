"""
URL configuration for schools project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from admissions.views import *
from transport.views import *
from profiles.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('products/',products,name="products"),
    path('services/',services,name="services"),
    path('login/',login,name="login"),
    path('trans/',trans,name="trans"),
    path('profiles/',profiles,name="profiles"),
    path('aboutus/',aboutus,name="aboutus")
]
