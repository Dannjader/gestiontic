# Generated by Django 5.0.6 on 2024-05-30 02:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Responsable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('cargo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Dispositivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.CharField(max_length=50)),
                ('tipo_dispositivo', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('activo_viejo', models.CharField(max_length=25, unique=True)),
                ('activo_nuevo', models.CharField(max_length=50, unique=True)),
                ('ubicacion', models.CharField(max_length=100)),
                ('responsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.responsable')),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_servicio', models.CharField(choices=[('error', 'Error'), ('mejora', 'Mejora'), ('nueva funcion', 'Nueva Funcion')], max_length=100)),
                ('requerimiento', models.CharField(max_length=200)),
                ('solucion', models.TextField(max_length=1000)),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='fecha_servicio')),
                ('dispositivos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.dispositivo')),
            ],
        ),
    ]
