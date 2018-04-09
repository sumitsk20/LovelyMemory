from django.db import models
from django.core.validators import RegexValidator


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


class CustomerOrderModel(models.Model):
    customer_name = models.CharField(max_length=100, blank=False, default='')
    customer_location = models.URLField(max_length=500, blank=False, default='')
    customer_note = models.TextField(max_length=1500, default='', blank=True, null=True)
    customer_deliver_date = models.DateField(blank=False, null=True, default=1970 / 1 / 1)
    customer_deliver_time = models.TimeField(blank=False, null=True, default='')
    phone_regex = RegexValidator(regex=r'^/d{9,15}$',
                                 message="Phone number must be entered in the format: '+9999'. Up to 15 digits allowed.")
    customer_phone_number = models.CharField(max_length=12, blank=True)
    customer_product_name = models.ForeignKey(Product, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.customer_name
