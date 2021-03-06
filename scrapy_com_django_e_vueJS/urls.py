"""scrapy_com_django_e_vueJS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django import urls
from django.contrib import admin
from django.db import router
from django.urls import path, include
from rest_framework import routers
from core.api.viewset import CitacoesViewSet


router = routers.DefaultRouter()
router.register(r'', CitacoesViewSet)


urlpatterns = [
    path('api/',include(router.urls)),
    path('admin/', admin.site.urls),
]
