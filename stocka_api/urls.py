from django.urls import path
from .views import ProductListView, ProductDetailView, CategoryListView, CategoryDetailView, VendorListView, VendorDetailView, SaleListView, PurchaseListView


urlpatterns = [
    path('products/', ProductListView.as_view()),
    path('products/<int:pk>/', ProductDetailView.as_view()),
    path('categories/', CategoryListView.as_view()),
    path('categories/<int:pk>/', CategoryDetailView.as_view()),
    path('vendors/', VendorListView.as_view()),
    path('vendors/<int:pk>/', VendorDetailView.as_view()),
    path('sales/', SaleListView.as_view()),
    path('purchases/', PurchaseListView.as_view()),
]
