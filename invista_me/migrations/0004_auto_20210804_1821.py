# Generated by Django 3.2.6 on 2021-08-04 21:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invista_me', '0003_auto_20210802_1255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investimento',
            name='ano_livro',
        ),
        migrations.RemoveField(
            model_name='investimento',
            name='autor_livro',
        ),
        migrations.RemoveField(
            model_name='investimento',
            name='autor_musica',
        ),
        migrations.AlterField(
            model_name='investimento',
            name='data',
            field=models.DateField(default=datetime.datetime(2021, 8, 4, 18, 21, 47, 494288)),
        ),
    ]
