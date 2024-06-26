# Generated by Django 5.0.1 on 2024-03-07 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminproductmanagement', '0003_alter_productvariant_unique_together'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('description', models.TextField()),
                ('minimum_amount', models.IntegerField()),
                ('discount_amount', models.IntegerField()),
                ('valid_from', models.DateField(auto_now_add=True)),
                ('valid_to', models.DateField()),
            ],
        ),
    ]
