# Generated by Django 3.2.7 on 2021-10-06 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='isActivo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='isAdmin',
            field=models.BooleanField(default=False),
        ),
    ]