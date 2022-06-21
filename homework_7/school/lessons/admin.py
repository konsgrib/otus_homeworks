from django.contrib import admin

from .models import (
    City,
    Product,
    # SchoolGroup,
    GroupType,
    ProductType,
    # Customer,
    # Student,
    # User,
    # Lesson,
)


admin.site.register(City)
admin.site.register(Product)
# admin.site.register(SchoolGroup)
admin.site.register(GroupType)

admin.site.register(ProductType)
# admin.site.register(Customer)
# admin.site.register(Student)
# admin.site.register(User)

# admin.site.register(Lesson)
