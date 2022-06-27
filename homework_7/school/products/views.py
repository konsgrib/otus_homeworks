from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm


def products(request):
    products = Product.objects.all()
    context = {
        "products": products,
    }
    return render(request, "products/products.html", context)


def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, "products/product.html", {"product": product})


def create_product(request):
    form = ProductForm()

    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("products")

    context = {"form": form}
    return render(request, "products/product_form.html", context)


def update_product(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("products")

    context = {"form": form}
    return render(request, "products/product_form.html", context)


def delete_product(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == "POST":
        product.delete()
        return redirect("products")
    context = {"object": product}
    return render(request, "delete_template.html", context)
