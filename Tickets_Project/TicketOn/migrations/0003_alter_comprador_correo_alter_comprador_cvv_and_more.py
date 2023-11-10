# Generated by Django 4.2.6 on 2023-11-10 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TicketOn', '0002_alter_evento_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comprador',
            name='correo',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='comprador',
            name='cvv',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='comprador',
            name='fecha_venc',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='comprador',
            name='nombre_titular',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='comprador',
            name='num_tarjeta',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='hora',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='eventos'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='lugar',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='organizador',
            name='correo',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='organizador',
            name='cuenta_clabe',
            field=models.CharField(max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='organizador',
            name='empresa',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]