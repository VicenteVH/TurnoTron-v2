# Generated by Django 5.0.3 on 2024-04-12 16:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0005_barbershop_closing_time_barbershop_opening_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='barber_shop',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='Clientes.barbershop'),
        ),
    ]
