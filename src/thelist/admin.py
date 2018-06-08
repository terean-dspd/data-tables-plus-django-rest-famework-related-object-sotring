from django.contrib import admin

# Register your models here.
from . import models


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'amount',
        'item',
        'client',
        ]

    class Meta:
        model = models.Order


class ClientAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'name'
        ]

    class Meta:
        model = models.Client

admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.Client, ClientAdmin)
