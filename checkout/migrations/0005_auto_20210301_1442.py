# Generated by Django 3.1.7 on 2021-03-01 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_order_customer_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer_number',
            field=models.CharField(max_length=50),
        ),
    ]
