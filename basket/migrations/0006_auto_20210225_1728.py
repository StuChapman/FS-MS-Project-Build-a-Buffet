# Generated by Django 3.1.7 on 2021-02-25 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0005_auto_20210222_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='servings',
            field=models.DecimalField(decimal_places=0, max_digits=3),
        ),
    ]