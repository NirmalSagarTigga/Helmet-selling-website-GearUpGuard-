# Generated by Django 4.2.4 on 2023-11-29 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helmets', '0004_order_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='total_price',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
    ]
