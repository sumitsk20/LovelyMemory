from django.contrib import admin
from .models import Product,CustomerOrderModel

# Register your models here.
admin.site.register(Product)
admin.site.register(CustomerOrderModel)
