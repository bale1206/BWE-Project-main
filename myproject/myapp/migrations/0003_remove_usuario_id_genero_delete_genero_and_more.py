# Generated by Django 5.0.6 on 2024-06-06 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_usuario_edad_alter_genero_genero_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='id_genero',
        ),
        migrations.DeleteModel(
            name='Genero',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]