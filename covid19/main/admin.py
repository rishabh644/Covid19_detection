from django.contrib import admin

# Register your models here.
from . import models
admin.site.register(models.Pdata)
admin.site.register(models.ImageModel)
