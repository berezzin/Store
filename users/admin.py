from django.contrib import admin

from products.admin import BasketInline
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)
    inlines = (BasketInline,)
    search_fields = ('username',)
