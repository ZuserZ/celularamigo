"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from .views import fcliente, Fcadcliente, salvar, excluir, exibir, update, flogcliente, logar, ftelacli, logout

urlpatterns = [
    path('', fcliente),
    path('Fcadcliente/',Fcadcliente, name='Fcadcliente'),
    path('salvar/', salvar, name='salvar'),
    path('excluir/<int:id>', excluir, name='excluir'),
    path('exibir/<int:id>', exibir, name='exibir'),
    path('exibir/', exibir, name='exibir'),
    path('update/<int:id>', update, name='update'),
    path('flogcliente', flogcliente, name='flogcliente'),
    path('logar', logar, name='logar'),
    path('ftelacli', ftelacli, name='ftelacli'),
    path('logout', logout, name='logout'),

]
