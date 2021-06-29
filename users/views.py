from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import permissions

from .models import CustomUser
from .serializers import CustomUserSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for the custom user.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    # permission_classes = permissions.IsAuthenticatedOrReadOnly

