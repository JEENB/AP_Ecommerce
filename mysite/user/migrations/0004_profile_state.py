# Generated by Django 3.1.2 on 2020-11-19 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20201110_0848'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='state',
            field=models.CharField(default='Haryana', max_length=50),
        ),
    ]
