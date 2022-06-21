from django.urls import path
from . import views

urlpatterns = [
    path("", views.products, name="products"),
    path("product/<int:pk>/", views.product, name="product"),
    path("create-product/", views.create_product, name="create-product"),
    path("update-product/<int:pk>/", views.update_product, name="update-product"),
    path("delete-product/<int:pk>/", views.delete_product, name="delete-product"),
]
