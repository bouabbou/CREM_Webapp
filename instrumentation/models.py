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

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Machine(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='machines')

    def __str__(self):
        return self.name

    def get_image_upload_path(self, filename):
        platform_abrv = self.category.platform.abbreviation
        category_abrv = self.category.abbreviation
        folder_name = f'infrastructure/{platform_abrv}/{category_abrv}/'
        return os.path.join(folder_name, filename)
"""
    def save(self, *args, **kwargs):
        if self.image:
            # Update the upload_to path before saving
            self.image.name = self.get_image_upload_path(self.image.name)
        super(Machine, self).save(*args, **kwargs)
"""
    def save(self, *args, **kwargs):
    	if self.image:
            upload_path = self.get_image_upload_path(self.image.name)
            self.image.storage.save(upload_path, self.image.file)
    	super(Machine, self).save(*args, **kwargs)
