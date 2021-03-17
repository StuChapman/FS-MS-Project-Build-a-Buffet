# Generated by Django 3.1.7 on 2021-03-17 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('item_number', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='item_number')),
                ('cookie', models.DecimalField(decimal_places=0, max_digits=8)),
                ('category', models.CharField(max_length=254)),
                ('name', models.CharField(max_length=254)),
                ('servings', models.DecimalField(decimal_places=0, max_digits=3)),
                ('option', models.CharField(max_length=254)),
                ('total_price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
            ],
        ),
    ]
