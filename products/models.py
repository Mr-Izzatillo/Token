from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.title

class Product(models.Model):
    categoryId = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    sellPrice = models.IntegerField()
    fullPrice = models.IntegerField()
    Image = models.ImageField(upload_to='product-images', default='product_pic.jpg')
    rating = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.title
    
    
