from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import OneToOneField


class CustomUserManager(models.Model):
    def create_user(self, email, password=None ):
        if not email:
            raise ValueError('User must have an email address') 
        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

        def create_superuser(self, email, password=None ):
            user = self.create_user(
                email,
                password=password,
            )

class User (models.Model):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    ) 

    is_active = models.BooleanField(default=True)
    is_venture = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


class Inventory(models.Model):
    product_Name = models.CharField(max_length=200)
    product_Image = models.ImageField(upload_to='product_images')
    product_Barcode = models.CharField(max_length=100)
    product_Category = models.CharField(max_length=100)
    selling_Price = models.IntegerField(default=0)
    cost_Price = models.IntegerField(default=0)
    product_Quantity = models.IntegerField(default=0)
    venture = models.ForeignKey ("Venture", on_delete=models.CASCADE)



class Venture(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

