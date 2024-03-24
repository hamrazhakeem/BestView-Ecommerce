# Generated by Django 4.2.7 on 2024-03-05 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminproductmanagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productvariant',
            name='color',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterUniqueTogether(
            name='productvariant',
            unique_together={('color', 'product')},
        ),
    ]