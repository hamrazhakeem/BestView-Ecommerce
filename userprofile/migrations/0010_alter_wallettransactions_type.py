# Generated by Django 5.0.1 on 2024-03-06 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0009_wallettransactions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallettransactions',
            name='type',
            field=models.CharField(choices=[('Debit', 'Debit'), ('Credit', 'Credit')]),
        ),
    ]