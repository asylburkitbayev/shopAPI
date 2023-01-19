from django.db import models
from datetime import date
from django.core.validators import MinValueValidator


class TypeProduct(models.Model):
    name = models.CharField(max_length=255, verbose_name='Тип продукта')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя категории')

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE,
                                 related_name='product_category')
    type_product = models.ForeignKey(TypeProduct, verbose_name='Тип продукта', on_delete=models.CASCADE,
                                     related_name='product_type')
    title = models.CharField(max_length=255, verbose_name='Наименование')
    image = models.ImageField(verbose_name='Изображение', null=True, upload_to='products/')
    description = models.TextField(verbose_name='Описание', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена', validators=[MinValueValidator(0)])
    date = models.DateField(verbose_name='Дата', default=date.today)
    percent_cashback = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=False, default=0)

    def __str__(self):
        return self.title

    @property
    def cashback(self):
        return self.price * self.percent_cashback / 100


class ProductImage(models.Model):
    image = models.ImageField(upload_to='products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')
