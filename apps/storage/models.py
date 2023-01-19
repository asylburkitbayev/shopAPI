from django.db import models
from apps.products.models import Product
from apps.branches.models import Branch


class Storage(models.Model):
    branch: Branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='branch_storage')
    product: Product = models.OneToOneField(Product, related_name='product_storage', verbose_name='Наименование товара',
                                         on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.branch.name} {self.product.title} {self.amount}"


class AddProductStorage(models.Model):
    storage: Storage = models.ForeignKey(Storage, on_delete=models.SET_NULL, null=True, related_name='add_storage')
    created_at = models.DateTimeField(auto_now_add=True)
    amount = models.PositiveIntegerField(default=1)

    def save(self, *args, **kwargs):
        self.storage.amount += self.amount
        self.storage.save()
        super().save(*args, **kwargs)
