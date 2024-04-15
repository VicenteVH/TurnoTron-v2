# Generated by Django 5.0.4 on 2024-04-09 20:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0004_appointment_is_expired'),
    ]

    operations = [
        migrations.AddField(
            model_name='barbershop',
            name='closing_time',
            field=models.TimeField(default=datetime.time(17, 0)),
        ),
        migrations.AddField(
            model_name='barbershop',
            name='opening_time',
            field=models.TimeField(default=datetime.time(8, 0)),
        ),
    ]
