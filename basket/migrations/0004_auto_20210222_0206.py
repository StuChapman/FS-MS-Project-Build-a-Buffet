# Generated by Django 3.1.7 on 2021-02-22 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0003_basket_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='total_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]
