# Generated by Django 4.2.7 on 2024-02-23 18:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_order_and_payment', '0005_alter_orderaddress_phone_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderaddress',
            name='phone_no',
            field=models.CharField(default=6767769754, max_length=10, validators=[django.core.validators.RegexValidator(message="Phone number must be 10 'digits'", regex='^\\d{10}$')]),
            preserve_default=False,
        ),
    ]
