# Generated by Django 5.0.6 on 2024-09-05 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispositivo',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='responsable',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]