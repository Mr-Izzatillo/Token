from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
from .models import Product, Category
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import ProductSerializers, CategorySerializers
from django.shortcuts import get_object_or_404

class ProductView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        product = Product.objects.all()
        serializer = ProductSerializers(instance=product, many = True)
        return Response(data=serializer.data)
    
    def post(self, request):
        serializer = ProductSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors, status=400)
    
    
class ProductDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, id):
        product = Product.objects.get(id=id)
        serializer = ProductSerializers(instance=product)
        return Response(data=serializer.data)
    
    
    def put(self, request, id):
        product = Product.objects.get(id=id)
        serializer = ProductSerializers(data=request.data, instance=product)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
    
    def patch(self, request, id):
        product = Product.objects.get(id=id)
        serializers = ProductSerializers(data=request.data, instance=product, partial = True)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data)
        return Response(data=serializers.errors)
    
    def delete(self, request, id):
        user = get_object_or_404(Product, id=id)
        user.delete()
        return Response(
            data={
                    'massage': "User delete"
            }
        )
    
    
    
class CategoryView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializers(instance=category, many = True)
        return Response(data=serializer.data)
    
    def post(self, request):
        serializer = CategorySerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors, status=400)
    
    
class CategoryDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, id):
        category = Category.objects.get(id=id)
        serializer = CategorySerializers(instance=category)
        return Response(data=serializer.data)
    
    
    def put(self, request, id):
        category = Category.objects.get(id=id)
        serializer = ProductSerializers(data=request.data, instance=category)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
    
    def patch(self, request, id):
        category = Category.objects.get(id=id)
        serializers = CategorySerializers(data=request.data, instance=category, partial = True)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data)
        return Response(data=serializers.errors)
    
    def delete(self, request, id):
        user = get_object_or_404(Category, id=id)
        user.delete()   
        return Response(
            data={
                    'massage': "PRODUCT delete"
            }
        )