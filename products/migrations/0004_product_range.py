# Generated by Django 3.1.6 on 2021-02-16 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210216_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='range',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]