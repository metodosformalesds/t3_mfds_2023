from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comprador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correo', models.CharField(max_length=30)),
                ('cvv', models.CharField(max_length=4)),
                ('num_tarjeta', models.CharField(max_length=16)),
                ('fecha_venc', models.DateField()),
                ('nombre_titular', models.CharField(max_length=100)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lugar', models.CharField(max_length=100)),
                ('hora', models.TimeField()),
                ('fecha', models.DateField()),
                ('nombre', models.CharField(max_length=100)),
                ('cupo', models.IntegerField()),
                ('imagen', models.ImageField(upload_to='eventos')),
                ('descripcion', models.TextField(max_length=1000)),
                ('tipo', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Organizador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correo', models.CharField(max_length=30)),
                ('empresa', models.CharField(max_length=30)),
                ('cuenta_clabe', models.CharField(max_length=18)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.FloatField()),
                ('estado', models.BooleanField(default=False)),
                ('codigo', models.CharField(max_length=30)),
                ('fecha_compra', models.DateField()),
                ('comprador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TicketOn.comprador')),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TicketOn.evento')),
            ],
        ),
        migrations.CreateModel(
            name='Transferencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('monto_final', models.FloatField()),
                ('estado', models.BooleanField(default=False)),
                ('comprador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TicketOn.comprador')),
                ('organizador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TicketOn.organizador')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TicketOn.ticket')),
            ],
        ),
        migrations.AddField(
            model_name='evento',
            name='organizador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TicketOn.organizador'),
        ),
    ]