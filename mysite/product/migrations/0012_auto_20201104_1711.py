# Generated by Django 3.1.2 on 2020-11-04 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_auto_20201104_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='filters',
            field=models.CharField(choices=[('Smart', 'Smart'), ('Computer', 'Computer'), ('Laptop', 'Laptop'), ('Accessories', 'Accessories')], max_length=18),
        ),
    ]
