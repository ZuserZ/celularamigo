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
from .views import fproduto, Fcadproduto, salvarP, excluirP, exibirP, updateP, exibir_celulares,exibir_capas, exibir_outros

urlpatterns = [
    path('', fproduto),
    path('Fcadproduto/',Fcadproduto, name='Fcadproduto'),
    path('salvarP/', salvarP, name='salvarP'),
    path('excluirP/<int:id>', excluirP, name='excluirP'),
    path('exibirP/<int:id>', exibirP, name='exibirP'),
    path('updateP/<int:id>', updateP, name='updateP'),
    path('exibir_celulares/', exibir_celulares, name='exibir_celulares'),
    path('exibir_capas/', exibir_capas, name='exibir_capas'),
    path('exibir_outros/', exibir_outros, name='exibir_outros'),


]


