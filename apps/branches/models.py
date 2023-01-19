from django.db import models
from apps.products.models import Category
from apps.users.models import User


class Branch(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название филиала')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    seller = models.OneToOneField(User, verbose_name='Продавец', on_delete=models.SET_NULL, null=True)
    list_categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name
