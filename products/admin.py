from django.contrib import admin

from .models import Product, Category, Subcategory


class ProductAdminConfig(admin.ModelAdmin):
    """Class **ProductAdminConfig** displays products list
    in admin panel based on :class`products.models.Product` model."""

    list_display = ("name", "price", "stock_count", "popularity", "rank", "sales_count")
    search_fields = ("name",)
    list_editable = ("price", "popularity", "rank", "stock_count")
    list_display_links = ("name",)
    save_on_top = True
    list_filter = ("created_at",)
    list_per_page = 50


class CategoryAdminConfig(admin.ModelAdmin):
    """Class **CategoryAdminConfig** displays categories list
    in admin panel based on :class`products.models.Category` model."""

    list_display = (
        "id",
        "name",
    )
    search_fields = ("name",)
    list_editable = ("name",)
    save_on_top = True
    list_per_page = 50


class SubcategoryAdminConfig(admin.ModelAdmin):
    """Class **SubcategoryAdminConfig** displays subcategories list
    in admin panel based on :class`products.models.Subcategory` model."""

    list_display = (
        "id",
        "name",
    )
    search_fields = ("name",)
    list_editable = ("name",)
    save_on_top = True
    list_per_page = 50


admin.site.register(Product, ProductAdminConfig)
admin.site.register(Category, CategoryAdminConfig)
admin.site.register(Subcategory, SubcategoryAdminConfig)
