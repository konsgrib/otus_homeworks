from django.urls import path
from .views import (
    ProductDetailView,
    ProductListView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)
from . import views


urlpatterns = [
    path("products", ProductListView.as_view(), name="products"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product"),
    path("create-product/", ProductCreateView.as_view(), name="create-product"),
    path(
        "update-product/<int:pk>/", ProductUpdateView.as_view(), name="update-product"
    ),
    path(
        "delete-product/<int:pk>/", ProductDeleteView.as_view(), name="delete-product"
    ),
]
