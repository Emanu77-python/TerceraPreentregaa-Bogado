# Generated by Django 5.0.6 on 2024-07-29 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='nacionalidad',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='autor',
            name='nombre',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='libro',
            name='titulo',
            field=models.CharField(max_length=30),
        ),
    ]
