# Generated by Django 4.1.5 on 2023-01-17 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0004_alter_storage_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addproductstorage',
            old_name='crated_at',
            new_name='created_at',
        ),
    ]
