# Generated by Django 5.0.1 on 2024-02-24 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_order_and_payment', '0011_alter_order_paymentmethod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='paymentmethod',
            field=models.CharField(choices=[('Cash On Delivery', 'Cash On Delivery'), ('PayPal', 'PayPal'), ('Wallet', 'Wallet')]),
        ),
    ]
