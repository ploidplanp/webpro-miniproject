# Generated by Django 3.0.3 on 2020-03-09 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_auto_20200309_1725'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_products',
            name='order_id',
        ),
        migrations.RemoveField(
            model_name='order_products',
            name='product_id',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Order_Products',
        ),
    ]
