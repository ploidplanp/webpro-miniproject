"""possite URL Configuration

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
from django.urls import include, path
from shop import views
app_name = 'shop'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.mylogin, name='mylogin'),
    path('logout', views.mylogout, name='mylogout'),
    path('shop/', include('shop.urls')),
    path('manage/', include('management.urls')),
    path('report/', include('reports.urls'))
]
