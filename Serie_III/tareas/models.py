from django.db import models

class Tarea(models.Model):
    PENDIENTE = 'pendiente'
    COMPLETADA = 'completada'
    ESTADOS = [
        (PENDIENTE, 'Pendiente'),
        (COMPLETADA, 'Completada'),
    ]

    titulo = models.CharField(max_length=200)
    curso = models.CharField(max_length=150)
    fechaEntrega = models.DateField()
    estado = models.CharField(max_length=10, choices=ESTADOS, default=PENDIENTE)

    def __str__(self):
        return self.titulo
