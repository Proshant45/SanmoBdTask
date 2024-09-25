from django.urls import path
from . import views

urlpatterns = [
    # Frontend Views
    path('', views.product_list, name='product_list'),
    path('all_product', views.all_product, name='all_product'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),

    # Admin CRUD Views with new prefix 'dashboard/'
    path('dashboard/products/', views.admin_product_list, name='admin_product_list'),
    path('dashboard/products/create/', views.admin_product_create, name='admin_product_create'),
    path('dashboard/products/<int:pk>/update/', views.admin_product_update, name='admin_product_update'),
    path('dashboard/products/<int:pk>/delete/', views.admin_product_delete, name='admin_product_delete'),
    path('accounts/register/', views.register, name='register'),
]










