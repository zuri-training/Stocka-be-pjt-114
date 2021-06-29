from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager

# Create your models here.

class CustomUser(AbstractUser):
    """ User Profile"""
    username = None
    email = models.EmailField(_('email address'), unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    business_name = models.CharField(max_length=255, blank=True, null=True)
    profile_pic = models.ImageField(
        upload_to='uploads/profile_pic/', null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  

    def __str__(self):
        return "{}".format(self.email)

