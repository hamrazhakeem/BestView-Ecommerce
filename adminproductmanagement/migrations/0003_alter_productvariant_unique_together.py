# Generated by Django 4.2.7 on 2024-03-05 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminproductmanagement', '0002_alter_productvariant_color_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='productvariant',
            unique_together=set(),
        ),
    ]
