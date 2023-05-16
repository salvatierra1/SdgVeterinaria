# Generated by Django 4.2.1 on 2023-05-08 16:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veterinaria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historiaclinica',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_alta',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 5, 8, 13, 57, 48, 584480), max_length=15, verbose_name='Fecha de alta'),
        ),
        migrations.AlterField(
            model_name='historiaclinica',
            name='fecha_consulta',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 5, 8, 13, 57, 48, 585479), max_length=15, verbose_name='Fecha de consulta'),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
    ]