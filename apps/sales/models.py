from django.db import models
from django.forms import ValidationError
from apps.storage.models import Storage
from apps.branches.models import Branch
from apps.products.models import Product
from apps.users.models import User


class Sale(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    client: User = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    sold = models.BooleanField(default=False)
    from_balance = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    @property
    def final_cashback(self):
        model = SaleProduct.objects.filter(sale=self)
        cashback = [i.total_cashback for i in model]
        if cashback:
            return sum(cashback)
        return 0

    @property
    def final_cost(self):
        model = SaleProduct.objects.filter(sale=self)
        cost = [i.total_cost for i in model]
        if cost:
            if self.from_balance:
                return sum(cost) - self.from_balance
            return sum(cost)
        return 0

    def clean(self):
        if self.sold:
            products = SaleProduct.objects.filter(sale=self).exists()
            if not products:
                raise ValidationError('sold не может быть '
                                      'True только после выбора товара для этой продажи')
        if self.client:
            if self.from_balance:
                if self.from_balance > self.client.cashback_all:
                    raise ValidationError('У клиента недостаточно баланса для использования')
        elif self.from_balance:
            raise ValidationError('Вы не можете использовать баланс, т.к пользователь не опознан')

    def save(self, *args, **kwargs):
        if self.sold:
            products = SaleProduct.objects.filter(sale=self).exists()
            if not products:
                from rest_framework.serializers import ValidationError
                raise ValidationError({'error': 'sold не может быть '
                                                'True только после выбора товара для этой продажи'})
            if self.client:
                cashback = CashBack.objects.filter(sale=self).exists()
                if not cashback:
                    CashBack.objects.create(sale=self)
            self.update_storage()

        super().save(*args, **kwargs)

    def update_storage(self):
        sale_products = SaleProduct.objects.filter(sale=self)
        for sale_product in sale_products:
            storage = Storage.objects.get(product=sale_product.product)
            storage.amount -= sale_product.amount
            storage.save()


class SaleProduct(models.Model):
    sale: Sale = models.ForeignKey(Sale, on_delete=models.CASCADE,
                                   related_name='product_sale')
    product: Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=1)

    def clean(self):
        if self.sale.sold:
            raise ValidationError('Продажа уже совершена, \
            Вы не можете больше добавлять продукты на эту продажу')

    @property
    def total_cost(self):
        return self.amount * self.product.price

    @property
    def total_cashback(self):
        return self.amount * self.product.cashback

    def __str__(self):
        return f"Продукт: {self.product.title} (для продаж)"


class CashBack(models.Model):
    sale: Sale = models.ForeignKey(Sale, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        user: User = self.sale.client
        user.cashback_all -= self.sale.from_balance
        user.cashback_all += self.sale.final_cashback
        user.save()
        super().save(*args, **kwargs)
