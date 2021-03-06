# Generated by Django 3.2.7 on 2021-10-07 23:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0002_historialdecompras_producto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historialdecompras',
            old_name='Id_Usuario',
            new_name='id',
        ),
        migrations.AddField(
            model_name='user',
            name='cellphone',
            field=models.CharField(default='NONE', max_length=15, verbose_name='Cellphone'),
        ),
        migrations.CreateModel(
            name='Tokens',
            fields=[
                ('Idtoken', models.AutoField(primary_key=True, serialize=False)),
                ('NombreCompleto', models.CharField(max_length=50)),
                ('Telefono', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('razon', models.IntegerField(choices=[(1, 'Producto'), (2, 'Entrega'), (3, 'Otra')], default=3)),
                ('comentario', models.TextField(max_length=500)),
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
