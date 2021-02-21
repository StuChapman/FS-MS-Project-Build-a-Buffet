# Generated by Django 3.1.7 on 2021-02-21 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cookie', models.DecimalField(decimal_places=0, max_digits=8)),
                ('category', models.CharField(max_length=254)),
                ('name', models.CharField(max_length=254)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('servings', models.DecimalField(decimal_places=0, max_digits=2)),
                ('option', models.CharField(max_length=254)),
            ],
        ),
    ]
