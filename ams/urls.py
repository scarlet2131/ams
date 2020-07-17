"""ams URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from login import views
from login import views as login_views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',login_views.login,name='login'),
    path('',login_views.login,name='login'),
    path('register/',login_views.register,name='register'),
    path('course/',login_views.course,name='course'),
    path('main/',login_views.main,name='main'),
    

    #allAuth
    path('accounts/', include('allauth.urls')),
    path('accounts/logout/',include('django.contrib.auth.urls')),

    #capture and Recognize
    path('imageRec/',login_views.imageRec,name='imageRec'),

    #ajax call
    path('main/pingDB/',login_views.pingDB,name='pingDB'),
    path('main/closeAttendance/',login_views.closeAttendance,name='closeAttendance')

  
]
