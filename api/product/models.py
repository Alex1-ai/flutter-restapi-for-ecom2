from distutils.command.upload import upload
from django.db import models
from api.category.models import Category
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=255)
    price = models.CharField(max_length=70)
    stock = models.CharField(max_length=70)
    is_active = models.BooleanField(default=True, blank=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True
        #Category, on_delete=models.CASCADE,
        #Category, on_delete=models.CASCADE

    )
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
