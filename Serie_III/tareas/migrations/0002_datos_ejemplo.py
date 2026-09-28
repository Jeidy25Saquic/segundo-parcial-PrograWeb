from django.db import migrations

def cargar_tareas(apps, schema_editor):
    Tarea = apps.get_model('tareas', 'Tarea')
    if not Tarea.objects.exists():
        Tarea.objects.create(titulo='Ensayo de historia', curso='Historia Universal', fechaEntrega='2026-10-05', estado='pendiente')
        Tarea.objects.create(titulo='Práctica de laboratorio', curso='Química', fechaEntrega='2026-09-28', estado='completada')

class Migration(migrations.Migration):
    dependencies = [('tareas', '0001_initial')]
    operations = [migrations.RunPython(cargar_tareas, migrations.RunPython.noop)]
