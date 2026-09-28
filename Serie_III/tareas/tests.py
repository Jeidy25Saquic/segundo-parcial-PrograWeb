from rest_framework import status
from rest_framework.test import APITestCase
from .models import Tarea

class TareaAPITests(APITestCase):
    def setUp(self):
        self.tarea = Tarea.objects.create(
            titulo='Proyecto final',
            curso='Programación Web',
            fechaEntrega='2026-10-10',
            estado='pendiente',
        )

    def test_consultar_todas(self):
        self.assertEqual(self.client.get('/api/tareas/').status_code, status.HTTP_200_OK)

    def test_consultar_una(self):
        self.assertEqual(self.client.get(f'/api/tareas/{self.tarea.id}/').status_code, status.HTTP_200_OK)

    def test_no_encontrada(self):
        self.assertEqual(self.client.get('/api/tareas/99999/').status_code, status.HTTP_404_NOT_FOUND)

    def test_filtrar_estado(self):
        self.assertEqual(self.client.get('/api/tareas/?estado=pendiente').status_code, status.HTTP_200_OK)

    def test_estado_invalido(self):
        self.assertEqual(self.client.get('/api/tareas/?estado=cancelada').status_code, status.HTTP_400_BAD_REQUEST)

    def test_completar(self):
        r = self.client.patch(f'/api/tareas/{self.tarea.id}/', {'estado':'completada'}, format='json')
        self.assertEqual(r.status_code, status.HTTP_200_OK)
        self.tarea.refresh_from_db()
        self.assertEqual(self.tarea.estado, 'completada')
