from django.db import models
import os

class Platform(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=10)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, related_name='categories')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='media/infrastructure/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name

    def get_image_upload_path(self, filename):
        # Get the platform name from the category's platform
        platform_name = self.category.platform.name
        # Define the directory structure
        folder_name = f'infrastructure/{platform_name}/'
        # Join the folder name with the filename
        return os.path.join(folder_name, filename)

    def save(self, *args, **kwargs):
        # Set the upload_to path dynamically based on the platform
        self.image.field.upload_to = self.get_image_upload_path(self.image.name)
        super(Product, self).save(*args, **kwargs)
