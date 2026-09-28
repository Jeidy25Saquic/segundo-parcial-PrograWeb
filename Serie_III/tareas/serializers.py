from rest_framework import serializers
from .models import Tarea

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = ['id', 'titulo', 'curso', 'fechaEntrega', 'estado']

class CompletarTareaSerializer(serializers.Serializer):
    estado = serializers.ChoiceField(choices=[Tarea.COMPLETADA])
