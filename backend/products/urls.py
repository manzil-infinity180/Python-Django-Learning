from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.product_view_details, name='product-list'),
    path('<int:pk>/update/', views.product_update_view),
    path('<int:pk>/delete/', views.product_delete_view),
    path('', views.product_create_view, name='product-views'),
    path('list-create', views.product_list_create_view, name='product-details')
]
