# Generated by Django 3.2.18 on 2023-03-13 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veg', '0005_vm'),
    ]

    operations = [
        migrations.CreateModel(
            name='reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('un', models.CharField(max_length=100)),
                ('em', models.EmailField(max_length=254)),
                ('p', models.CharField(max_length=100)),
                ('cp', models.CharField(max_length=100)),
            ],
        ),
    ]
