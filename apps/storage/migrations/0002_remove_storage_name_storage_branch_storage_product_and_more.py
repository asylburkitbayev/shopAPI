# Generated by Django 4.1.5 on 2023-01-17 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('branches', '0001_initial'),
        ('products', '0001_initial'),
        ('storage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storage',
            name='name',
        ),
        migrations.AddField(
            model_name='storage',
            name='branch',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='branch_storage', to='branches.branch'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='storage',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='product_storage', to='products.product', verbose_name='Наименование товара'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='storage',
            name='amount',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='AddProductStorage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crated_at', models.DateTimeField(auto_now_add=True)),
                ('amount', models.PositiveIntegerField(default=1)),
                ('storage', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='add_storage', to='storage.storage')),
            ],
        ),
    ]
