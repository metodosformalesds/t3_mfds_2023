# Generated by Django 4.2.6 on 2023-11-10 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TicketOn', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='tipo',
            field=models.CharField(max_length=20),
        ),
    ]
