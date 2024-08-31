from .models import Product, Category
from rest_framework import serializers

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'categoryId', 'title', 'sellPrice', 'fullPrice', 'rating']
        
        
class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']