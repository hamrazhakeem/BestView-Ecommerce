# Generated by Django 4.2.7 on 2024-02-18 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usershome', '0003_alter_customuser_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_no',
            field=models.CharField(unique=True),
        ),
    ]