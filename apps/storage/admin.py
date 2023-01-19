from django.contrib.admin import ModelAdmin, register

from apps.storage.models import Storage, AddProductStorage


@register(Storage)
class StorageAdmin(ModelAdmin):
    list_display = ('branch', 'product', 'amount')


@register(AddProductStorage)
class AddProductStorageAdmin(ModelAdmin):
    list_display = ('storage', 'amount', 'created_at')
