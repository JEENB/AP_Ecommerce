# Generated by Django 3.1.2 on 2020-11-19 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20201119_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.CharField(default='India', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='state',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
