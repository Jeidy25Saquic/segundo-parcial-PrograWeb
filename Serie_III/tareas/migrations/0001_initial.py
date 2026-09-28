from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('curso', models.CharField(max_length=150)),
                ('fechaEntrega', models.DateField()),
                ('estado', models.CharField(choices=[('pendiente','Pendiente'),('completada','Completada')], default='pendiente', max_length=10)),
            ],
        ),
    ]
