# Generated by Django 4.1.3 on 2023-02-07 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0013_remove_producto_cantidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagentarea',
            name='imagen',
            field=models.FileField(upload_to='Chimeneas'),
        ),
        migrations.AlterField(
            model_name='imagentarea',
            name='tarea',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='archivos', to='tareas.tarea'),
        ),
        migrations.RemoveField(
            model_name='tarea',
            name='imagen',
        ),
        migrations.AddField(
            model_name='tarea',
            name='imagen',
            field=models.ManyToManyField(blank=True, related_name='archivos', to='tareas.imagentarea'),
        ),
    ]