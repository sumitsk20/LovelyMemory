from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=250, blank=False)
    description = models.TextField(max_length=1500)
    image = models.ImageField(upload_to='product_image', blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    modificationTime = models.DateField(auto_now=True)

    BALLOON = 'BL'
    GIFT = 'GF'
    FLOWER = 'FW'
    TYPE_OF_PRODUCT = (
        (BALLOON, 'balloon'),
        (GIFT, 'gift'),
        (FLOWER, 'flower'),
    )
    type_product = models.CharField(max_length=2,
                            choices=TYPE_OF_PRODUCT,
                            default=FLOWER)

    def __str__(self):
        return self.name


class CustomerOrder(models.Model):
    customer_name = models.CharField(max_length=100, blank=False, default='')
    customer_location = models.CharField(max_length=500, blank=False, default='')
    customer_request = models.TextField(max_length=1500)
    customer_deliver = models.DateField()

    def __str__(self):
        return self.customer_name
