# Generated by Django 4.2.7 on 2023-11-18 01:56

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("TicketOn", "0005_evento_precio"),
    ]

    operations = [
        migrations.AlterField(
            model_name="evento",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                always_update=True, editable=False, populate_from="nombre", unique=True
            ),
        ),
    ]