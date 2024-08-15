from django.db import models

class Platform(models.Model):
    name = models.CharField(max_length=255)

    def _str_(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=10)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, related_name='categories')

    def _str_(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def _str_(self):
        return self.name