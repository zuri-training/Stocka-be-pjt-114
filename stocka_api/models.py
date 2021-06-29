from django.db import models
from stocka_project import settings

# Create your models here.
# QUANTITY_TYPE = (
#     ('PU', 'Per Unit'),
#     ('PC', 'Per Carton')
# )


# class Vendor(models.Model):
#     name = models.CharField(max_length=255)
#     phone_number = models.CharField(max_length=11)   # can be used for phone number

#     def __str__(self):
#         return self.name


# class Category(models.Model):
#     name = models.CharField(max_length=255)

#     class Meta:
#         verbose_name_plural = "Categories"

#     def __str__(self):
#         return self.name


# class ProductBarcode(models.Models):
#     barcode = models.CharField(
#         max_length=255, null=True, blank=True, unique=True)


# class Product(models.Model):
#     item_name = models.CharField(max_length=255,unique=True)
#     item_category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     item_image = models.ImageField(upload_to='uploads/category/items/', null=True, blank=True)
#     cost_price = models.DecimalField(max_digits=12, decimal_places=2)
#     selling_price = models.DecimalField(max_digits=12, decimal_places=2)
#     vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=0)
#     quantity_type = models.CharField(max_length=2, choices=QUANTITY_TYPE)
#     barcode = models.OneToOneField(ProductBarcode, on_delete=models.CASCADE)


#     def __str__(self):
#         return self.item_name


# class Sale(models.Model):
#     item = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=0, null=True, blank=True)
#     quantity_type = models.CharField(max_length=2, choices=QUANTITY_TYPE)
#     selling_price = models.DecimalField(max_digits=12, decimal_places=2)
#     barcode = models.OneToOneField(ProductBarcode, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.item.item_name


# class Purchase(models.Model):
#     item = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=0, null=True, blank=True)
#     quantity_type = models.CharField(max_length=2, choices=QUANTITY_TYPE)
#     cost_price = models.DecimalField(max_digits=12, decimal_places=2)
#     barcode = models.OneToOneField(ProductBarcode, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.item.item_name
