from django.urls import path
from . import views

urlpatterns = [
    path('home/<str:do_what>', views.home, name='home'),
]