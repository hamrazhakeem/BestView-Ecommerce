# Generated by Django 5.0.1 on 2024-03-10 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminproductmanagement', '0014_remove_categoryoffer_status_categoryoffer_is_listed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoryoffer',
            name='discount_percentage',
            field=models.IntegerField(default=0),
        ),
    ]
