from django.urls import path
from . import views

urlpatterns = [
    path('show/<str:reportlist>', views.show, name='show'),
]