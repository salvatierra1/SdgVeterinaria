# Generated by Django 4.2 on 2023-05-09 14:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veterinaria', '0002_historiaclinica_estado_alter_cliente_fecha_alta_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='telefono',
            field=models.PositiveIntegerField(blank=True, max_length=15, null=True, verbose_name='Telefono'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_alta',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 5, 9, 11, 29, 18, 457864), max_length=15, verbose_name='Fecha de alta'),
        ),
        migrations.AlterField(
            model_name='historiaclinica',
            name='fecha_consulta',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 5, 9, 11, 29, 18, 463019), max_length=15, verbose_name='Fecha de consulta'),
        ),
    ]