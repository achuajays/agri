# Generated by Django 4.1.5 on 2023-03-11 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('p_id', models.IntegerField(primary_key=True, serialize=False)),
                ('p_na', models.CharField(max_length=100)),
                ('p_dis', models.CharField(max_length=100)),
                ('p_loc', models.CharField(max_length=100)),
                ('p_sn', models.CharField(max_length=100)),
                ('p_pr', models.FloatField()),
                ('p_ph', models.IntegerField()),
                ('p_da', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='reconfigure',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('na', models.CharField(max_length=100)),
                ('dis', models.CharField(max_length=100)),
                ('loc', models.CharField(max_length=100)),
                ('sn', models.CharField(max_length=100)),
                ('pr', models.FloatField()),
                ('ph', models.IntegerField()),
                ('da', models.DateField()),
            ],
        ),
    ]