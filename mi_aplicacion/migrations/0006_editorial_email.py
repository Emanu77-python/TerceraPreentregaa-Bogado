# Generated by Django 5.0.6 on 2024-07-30 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_aplicacion', '0005_remove_libro_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='editorial',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]