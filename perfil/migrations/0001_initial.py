# Generated by Django 4.0.1 on 2022-01-19 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40)),
                ('title', models.CharField(max_length=40)),
                ('content', models.TextField()),
                ('imagen', models.CharField(max_length=255)),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=60)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=255)),
                ('imagen_perfil', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=255)),
                ('descripcion', models.CharField(max_length=255)),
                ('admin', models.BooleanField()),
            ],
        ),
    ]
