from django.urls import path
from .views import index, product_detail

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
]