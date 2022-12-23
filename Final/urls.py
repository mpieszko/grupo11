"""Final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from .settings import *
from django.contrib.auth.views import LoginView,logout_then_login
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from App.noticias.models import  Contacto


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Index),
    path('inicio/',Index,name='inicio'),
    path('',include('App.noticias.urls',namespace='noticias')),
    path('',include('App.usuario.urls')),
    path('nosotros/',nosotros),
    # path('password',password),
    path('donaciones/',donaciones),
    path('contacto/', views.Contacto , name = 'Contacto'),
    # path('register/',views.registerPage, name= "register"),
    # path('login/',views.loginPage, name= "login"),
    # path('logout/',views.logoutUser, name= "logout"),
] 
static(STATIC_URL, document_root = STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)