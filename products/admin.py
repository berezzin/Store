from django.contrib import admin
from products.models import Category, Product, Basket


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'quantity')

    fields = ('name', 'description', ('price', 'quantity'), 'image', 'category')

    search_fields = ('name',)

    ordering = ('name',)


class BasketInline(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0


admin.site.register([Category])
