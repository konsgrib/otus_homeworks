from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Product


class ProductDetailView(DetailView):
    model = Product


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.select_related("city", "type")
        return qs


class ProductCreateView(CreateView):
    model = Product
    fields = "__all__"


class ProductUpdateView(UpdateView):
    model = Product
    fields = "__all__"


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("products")
