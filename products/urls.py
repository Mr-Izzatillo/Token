from django.urls import path
from .views import ProductView, ProductDetail, CategoryView, CategoryDetail

app_name = 'products'

urlpatterns = [
    path('product/', ProductView.as_view(), name='product'),
    path('product/<int:id>/', ProductDetail.as_view(), name='product_detail'),
    path('category/', CategoryView.as_view(), name='category'),
    path('category/<int:id>/', CategoryDetail.as_view(), name='category_detail')
]
