# Generated by Django 3.1.6 on 2021-02-16 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210216_1502'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='has_sizes',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
    ]
