# Generated by Django 4.1.5 on 2023-11-19 05:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("TicketOn", "0016_carrito"),
    ]

    operations = [
        migrations.AddField(
            model_name="carrito",
            name="monto_final",
            field=models.FloatField(default=0.0),
        ),
    ]
