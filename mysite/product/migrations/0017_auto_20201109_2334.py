# Generated by Django 3.1.2 on 2020-11-09 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_auto_20201107_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.URLField(default=''),
        ),
        migrations.DeleteModel(
            name='Reviews',
        ),
    ]
