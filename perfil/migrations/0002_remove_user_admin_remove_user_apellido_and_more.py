# Generated by Django 4.0.1 on 2022-01-19 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='admin',
        ),
        migrations.RemoveField(
            model_name='user',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='user',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.RemoveField(
            model_name='user',
            name='imagen_perfil',
        ),
        migrations.RemoveField(
            model_name='user',
            name='link',
        ),
        migrations.RemoveField(
            model_name='user',
            name='nombre',
        ),
    ]
