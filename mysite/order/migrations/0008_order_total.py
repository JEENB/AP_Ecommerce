# Generated by Django 3.1.2 on 2020-11-19 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_order_orderproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.FloatField(null=True),
        ),
    ]