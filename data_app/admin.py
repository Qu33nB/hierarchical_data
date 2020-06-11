from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from data_app.models import Data
# Register your models here.

admin.site.register(Data, MPTTModelAdmin)
