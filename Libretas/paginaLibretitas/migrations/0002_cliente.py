# Generated by Django 5.0.6 on 2024-07-03 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginaLibretitas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('rutCliente', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombreCliente', models.CharField(max_length=100)),
                ('emailCliente', models.EmailField(max_length=50, unique=True)),
                ('direccionCliente', models.CharField(max_length=100)),
                ('fechaNacimientoCliente', models.DateField()),
                ('contraseña', models.CharField(max_length=50)),
            ],
        ),
    ]
