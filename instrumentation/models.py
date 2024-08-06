from django.db import models

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=10) 
    platform = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name
