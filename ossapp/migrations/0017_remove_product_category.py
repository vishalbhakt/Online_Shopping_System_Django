# Generated by Django 4.1 on 2022-08-29 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ossapp', '0016_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
    ]