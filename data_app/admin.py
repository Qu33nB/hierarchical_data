from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from data_app.models import Data

admin.site.register(Data, DraggableMPTTAdmin)
