# Generated by Django 4.2.1 on 2023-05-27 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTienda', '0005_posteo_reserva_posteo_user_reserva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posteo',
            name='reserva',
            field=models.BooleanField(default=False),
        ),
    ]
