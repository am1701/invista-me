# Generated by Django 3.2.6 on 2021-08-04 21:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invista_me', '0005_auto_20210804_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investimento',
            name='data',
            field=models.DateField(default=datetime.datetime(2021, 8, 4, 18, 27, 11, 668448)),
        ),
        migrations.AlterField(
            model_name='investimento',
            name='investimento',
            field=models.TextField(max_length=15),
        ),
    ]
