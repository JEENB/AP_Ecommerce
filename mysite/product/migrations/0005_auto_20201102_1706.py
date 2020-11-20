# Generated by Django 3.1.2 on 2020-11-02 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20201102_1528'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='amount',
            new_name='quantity',
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('imgDescription', models.CharField(max_length=50)),
                ('a', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]