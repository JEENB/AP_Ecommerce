# Generated by Django 3.1.2 on 2020-11-12 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20201110_1002'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='product',
            new_name='products',
        ),
    ]
