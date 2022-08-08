from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=255)
    cart_image = models.ImageField(upload_to='categories/photos', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

# TODO:
