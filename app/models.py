from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Registration(AbstractUser):
    is_user = models.BooleanField(default=False)
    name = models.CharField(max_length=50,null=True)
    email = models.EmailField(max_length=254)
    contact_no = models.CharField(max_length=50,null=True)
    profile = models.ImageField(upload_to=None, null=True)


