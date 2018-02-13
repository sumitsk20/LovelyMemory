from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=250, blank=False)
    type = models.CharField(max_length=250)
    description = models.TextField(max_length=1500)
    image = models.ImageField(upload_to='product_image', blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    quantity = models.DecimalField(max_digits=3, decimal_places=0, default=0)

    def __str__(self):
        return self.name
