# Generated by Django 4.2.7 on 2023-11-19 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TicketOn', '0017_carrito_monto_final'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrito',
            name='monto_final',
        ),
    ]