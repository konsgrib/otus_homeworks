from django.db import models
from django.urls import reverse


class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["name"]


class ProductType(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.title}: {self.description}"


class Product(models.Model):
    type = models.ForeignKey("ProductType", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    city = models.ForeignKey("City", on_delete=models.CASCADE)
    price = models.FloatField(null=False)
    # created_by = models.ForeignKey("User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse("product", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.city.name}: {self.title}, {self.price}"
