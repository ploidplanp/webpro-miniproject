from django.urls import path
from . import views

urlpatterns = [
    path('product/', views.manage, name='manage'),
    path('add/product/', views.add_product, name='add_product'),
    path('add/type/', views.add_type, name='add_type'),
    path('edit/product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('edit/type/<int:type_id>/', views.edit_type, name='edit_type'),
    path('delete/type/<int:type_id>/', views.delete_type, name='delete_type'),
    path('delete/product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('type/list', views.alltype, name='alltype')
]