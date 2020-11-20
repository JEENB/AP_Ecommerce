# Generated by Django 3.1.2 on 2020-11-19 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_auto_20201119_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Placed', 'Placed'), ('Accepted', 'Accepted'), ('Shipping', 'Shipping'), ('Complete', 'Complete'), ('Canceled', 'Canceled')], default='Placed', max_length=20),
        ),
    ]
