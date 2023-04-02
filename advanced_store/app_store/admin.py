from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


class BasketAdminInline(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category', 'get_html_photo')
    fields = ('name', 'image', 'description', 'short_description', ('price', 'quantity'), 'category')
    # readonly_fields = ('short_description',)
    ordering = ['-name']
    search_fields = ['name']

    def get_html_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=30>")
        else:
            return "Нет фото"

    get_html_photo.short_description = "Миниатюра"


admin.site.register(ProductCategory)
# admin.site.register(Product, ProductAdmin)
admin.site.register(Basket)
