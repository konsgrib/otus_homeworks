from django.contrib import admin

from .models import (
    City,
    ProductType,
    Product,
)


admin.site.register(City)
admin.site.register(ProductType)
admin.site.register(Product)
