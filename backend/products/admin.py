from django.contrib import admin
from django.contrib.admin import ModelAdmin

from . import models


class ProductAdminConfig(ModelAdmin):
    model = models.Product

    search_fields = ('name', 'price', 'description')
    list_filter = ('name', 'price', 'description')
    # ordering = ('-price',)
    list_display = ('name', 'price', 'description')


admin.site.register(models.Product, ProductAdminConfig)
