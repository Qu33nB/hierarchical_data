from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.
class Data(MPTTModel):
    name = models.CharField(max_length=200,unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


# Create your models here.
class CustomUser(AbstractUser):
    display_name = models.CharField(max_length=50, null=True, blank=True)
    homepage = models.URLField(max_length=200, null=True, blank=True)

    REQUIRED_FIELDS = ['display_name', 'homepage']

    def __str__(self):
        return self.name
