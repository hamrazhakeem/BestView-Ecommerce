# Generated by Django 4.2.7 on 2024-02-18 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usershome', '0004_alter_customuser_phone_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_no',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]