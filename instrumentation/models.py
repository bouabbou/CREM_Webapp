from django.db import models
import os

class Platform(models.Model):
    name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=10, default="N/A")

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=10)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, related_name='categories')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)  # Added max_length here
    description = models.TextField()
    image = models.ImageField(upload_to='infrastructure/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name

    def get_image_upload_path(self, filename):
        platform_name = self.category.platform.name
        folder_name = f'infrastructure/{platform_name}/'
        return os.path.join(folder_name, filename)

    def save(self, *args, **kwargs):
        # Ensure the upload_to path is set correctly
        if self.image and self.image.name:
            self.image.field.upload_to = self.get_image_upload_path(self.image.name)
        super(Product, self).save(*args, **kwargs)
