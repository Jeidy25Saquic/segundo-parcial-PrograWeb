from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Tarea
from .serializers import TareaSerializer, CompletarTareaSerializer

class TareaListAPIView(APIView):
    def get(self, request):
        estado = request.query_params.get('estado')
        if estado is not None and estado not in {Tarea.PENDIENTE, Tarea.COMPLETADA}:
            return Response(
                {'error': 'Estado inválido', 'detalle': "El estado debe ser 'pendiente' o 'completada'."},
                status=status.HTTP_400_BAD_REQUEST
            )

        tareas = Tarea.objects.all().order_by('id')
        if estado:
            tareas = tareas.filter(estado=estado)

        return Response(TareaSerializer(tareas, many=True).data, status=status.HTTP_200_OK)

class TareaDetailAPIView(APIView):
    def obtener(self, tarea_id):
        try:
            return Tarea.objects.get(id=tarea_id)
        except Tarea.DoesNotExist:
            return None

    def get(self, request, tarea_id):
        tarea = self.obtener(tarea_id)
        if tarea is None:
            return Response({'error': 'No existe una tarea con ese id'}, status=status.HTTP_404_NOT_FOUND)
        return Response(TareaSerializer(tarea).data, status=status.HTTP_200_OK)

    def patch(self, request, tarea_id):
        tarea = self.obtener(tarea_id)
        if tarea is None:
            return Response({'error': 'No existe una tarea con ese id'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CompletarTareaSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'error': 'Body inválido', 'detalle': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        tarea.estado = Tarea.COMPLETADA
        tarea.save(update_fields=['estado'])
        return Response(TareaSerializer(tarea).data, status=status.HTTP_200_OK)
