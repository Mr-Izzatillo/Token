from django.shortcuts import render
from .models import Order
from rest_framework.views import APIView
from .serializers import OrderSerializers
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404


class OrderView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        order = Order.objects.all()
        serializers = OrderSerializers(instance=order, many = True)
        return Response(data=serializers.data)
    
    def post(self, request):
        serializer = OrderSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors, status=400)
    
    
class OrderDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        order = Order.objects.all()
        serializer = OrderSerializers(instance=order, many = True)
        return Response(data=serializer.data)

    def put(self, request, id):
        order = Order.objects.get(id=id)
        serializer = OrderSerializers(data=request.data, instance=order)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
    
    def patch(self, request, id):
        order = Order.objects.get(id=id)
        serializers = OrderSerializers(data=request.data, instance=order, partial = True)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data)
        return Response(data=serializers.errors)
    
    def delete(self, request, id):
        user = get_object_or_404(Order, id=id)
        user.delete()
        return Response(
            data={
                    'massage': "PRODUCT delete"
            }
        )