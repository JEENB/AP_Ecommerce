# Generated by Django 3.1.2 on 2020-11-12 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_auto_20201109_2334'),
    ]

    operations = [
        migrations.RenameField(
            model_name='images',
            old_name='product_title',
            new_name='product',
        ),
    ]
