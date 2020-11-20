# Generated by Django 3.1.2 on 2020-11-03 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(blank=True, max_length=100)),
                ('body', models.CharField(max_length=1000)),
                ('contact', models.IntegerField()),
                ('status', models.CharField(choices=[('Open', 'Open'), ('Read', 'Read'), ('Resolved', 'Resolved')], default='Open', max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('notes', models.CharField(blank=True, max_length=1000)),
            ],
        ),
    ]