# Generated by Django 3.1.2 on 2020-11-21 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0020_auto_20201118_2233'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='keywords',
            new_name='brand',
        ),
    ]
