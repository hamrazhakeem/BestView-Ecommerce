# Generated by Django 5.0.1 on 2024-03-11 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminproductmanagement', '0017_remove_categoryoffer_is_listed_categoryoffer_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='offer_price',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
    ]