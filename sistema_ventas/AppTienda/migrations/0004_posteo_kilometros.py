# Generated by Django 4.2.1 on 2023-05-27 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTienda', '0003_alter_posteo_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='posteo',
            name='kilometros',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]