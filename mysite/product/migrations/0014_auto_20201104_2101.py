# Generated by Django 3.1.2 on 2020-11-04 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_auto_20201104_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('SmartPhones', 'SmartPhones'), ('Computer', 'Computer'), ('Laptop', 'Laptop'), ('Accessories', 'Accessories')], max_length=18),
        ),
    ]