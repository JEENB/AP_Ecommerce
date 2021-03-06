# Generated by Django 3.1.2 on 2020-11-19 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20201119_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='contact',
            field=models.DecimalField(decimal_places=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pincode',
            field=models.DecimalField(decimal_places=0, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='state',
            field=models.CharField(default='Haryana', max_length=50, null=True),
        ),
    ]
