from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class GroupType(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.title}: {self.description}"


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

    def __str__(self):
        return f"{self.title}, {self.price}"


# class SchoolGroup(models.Model):
#     title = models.CharField(max_length=100)
#     teacher = models.ForeignKey("User", on_delete=models.CASCADE)
#     type = models.ForeignKey("GroupType", on_delete=models.CASCADE)
#     city = models.ForeignKey("City", on_delete=models.CASCADE)
#     duration = models.IntegerField(null=False)
#     invoice_string = models.CharField(max_length=200)
#     student = models.ManyToManyField("Student", blank=True)
#     product = models.ManyToManyField("Product", blank=True)
#     # created_by = models.ForeignKey("User", on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     active = models.BooleanField(default=True)

#     def __str__(self):
#         return f"city:{self.city}, {self.name}, duration: {self.duration}"


# class Customer(models.Model):
#     name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     ssn = models.CharField(max_length=12)
#     phone = models.CharField(max_length=13)
#     email = models.CharField(max_length=100)
#     want_invoice = models.BooleanField(default=True)
#     created_by = models.ForeignKey("User", on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     active = models.BooleanField(default=True)

#     def __str__(self):
#         return (
#             f"{self.last_name},{self.name} {self.phone}{self.email}{self.want_invoice}"
#         )


# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     ssn = models.CharField(max_length=12)
#     phone = models.CharField(max_length=13)
#     email = models.CharField(max_length=100)
#     customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
#     created_by = models.ForeignKey("User", on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     active = models.BooleanField(default=True)

#     def __str__(self):
#         return f"{self.last_name},{self.name} {self.phone}{self.email}"


# class User(models.Model):
#     username = models.CharField(max_length=20)
#     name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     ssn = models.CharField(max_length=12)
#     phone = models.CharField(max_length=13)
#     email = models.CharField(max_length=100)
#     # created_by = models.ForeignKey("User", on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     active = models.BooleanField(default=True)

#     def __str__(self):
#         return f"{self.last_name},{self.name} {self.phone}{self.email}"


# class Lesson(models.Model):
#     type = models.CharField(max_length=100)
#     description = models.TextField(null=True, blank=True)
#     teacher_id = models.ForeignKey("User", on_delete=models.CASCADE)
#     date_happenned = models.DateField(null=False)
#     group_id = models.ForeignKey("SchoolGroup", on_delete=models.CASCADE)
#     # created_by = models.ForeignKey("User", on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     active = models.BooleanField(default=True)

#     def __str__(self):
#         return f"{self.date_happenned} - {self.description}"
