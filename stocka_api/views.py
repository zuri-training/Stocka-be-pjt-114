from django.shortcuts import render
from .serializers import (
    ProductSerializer, SaleSerializer, 
    PurchaseSerializer, VendorSerializer, CategorySerializer
)
from .models import (
    Product, Sale, Purchase, Vendor, Category
)
from rest_framework.response import Response
from rest_framework import generics, status, permissions

# Create your views here.

# Lists all products and creates product instances
class ProductListView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    

# Retrieves, updates and deletes product instances
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

# Lists all vendors and creates vendor instances
class VendorListView(generics.ListCreateAPIView):
    serializer_class = VendorSerializer
    queryset = Vendor.objects.all()

# Retrieves, updates and deletes vendor instances
class VendorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VendorSerializer
    queryset = Vendor.objects.all()

# Lists all product categories and creates product category instances
class CategoryListView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

# Retrieves, updates and deletes product category instances
class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

# # Lists all product barcodes and creates product category instances
# class ProductBarcodeListView(generics.ListCreateAPIView):
#     serializer_class = ProductBarcodeSerializer
#     queryset = ProductBarcode.objects.all()

# # Retrieves, updates and deletes product barcodes instances
# class ProductBarcodeDetailView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = ProductBarcodeSerializer
#     queryset = ProductBarcode.objects.all()

# Lists all sales and creates sale instances
class SaleListView(generics.ListCreateAPIView):
    serializer_class = SaleSerializer
    queryset = Sale.objects.all()

# # Retrieves, updates and deletes product barcodes instances
# class SaleDetailView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = SaleSerializer
#     queryset = Sale.objects.all()

# Lists all purchases and creates purchase instances
class PurchaseListView(generics.ListCreateAPIView):
    serializer_class = PurchaseSerializer
    queryset = Purchase.objects.all()


# class PurchaseDetailView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = PurchaseSerializer
#     queryset = Purchase.objects.all()
