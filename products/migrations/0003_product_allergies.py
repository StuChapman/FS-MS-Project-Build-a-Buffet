# Generated by Django 3.1.7 on 2021-04-03 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210326_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='allergies',
            field=models.CharField(max_length=4, null=True),
        ),
    ]