from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import generics, permissions, status

from .models import CustomUser
from .serializers import CustomUserSerializer

from django.urls import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response


class CustomUserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for the custom user.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    # permission_classes = permissions.IsAuthenticated

