# Generated by Django 4.1.3 on 2023-03-21 20:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tareas', '0029_visitas_alter_tarea_completado_alter_tarea_proveedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='modelo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tareas.producto'),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='proveedor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='tareas.proveedor'),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
