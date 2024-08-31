from django.urls import path
from .views import OrderView, OrderDetail
app_name = 'order'
urlpatterns = [
    path('order/', OrderView.as_view(), name = 'order'),
    path('order/<int:id>/', OrderDetail.as_view(), name='order_detail'),
]
