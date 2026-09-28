from django.urls import path
from .views import TareaListAPIView, TareaDetailAPIView

urlpatterns = [
    path('', TareaListAPIView.as_view(), name='tareas-list'),
    path('<int:tarea_id>/', TareaDetailAPIView.as_view(), name='tareas-detail'),
]
