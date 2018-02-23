from django.contrib import admin
from .models import Product,CustomerOrder

# Register your models here.
admin.site.register(Product)
admin.site.register(CustomerOrder)
