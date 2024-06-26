# Generated by Django 5.0.2 on 2024-03-24 00:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_pais', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Puesto_trabajo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_pu', models.CharField(max_length=30)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Salarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_bruto', models.IntegerField()),
                ('extra_dec', models.BooleanField(default=False)),
                ('extra_jun', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Poblacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_pob', models.CharField(max_length=40)),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.pais')),
            ],
        ),
        migrations.CreateModel(
            name='Fabricas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_fab', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=30)),
                ('codigo_postal', models.IntegerField()),
                ('poblacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.poblacion')),
            ],
        ),
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_em', models.CharField(max_length=30)),
                ('documento', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('direccion_em', models.CharField(max_length=30)),
                ('fabrica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.fabricas')),
                ('puesto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.puesto_trabajo')),
            ],
        ),
        migrations.AddField(
            model_name='puesto_trabajo',
            name='salarios',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.salarios'),
        ),
    ]
