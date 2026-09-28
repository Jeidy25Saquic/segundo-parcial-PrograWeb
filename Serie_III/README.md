# Serie III

API de tareas desarrollada con Django y Django REST Framework.

## Contrato de API

| Acción | Método HTTP | Endpoint |
|---|---|---|
| Consultar tareas | GET | `/api/tareas/` |
| Consultar una tarea | GET | `/api/tareas/{id}/` |
| Filtrar por estado | GET | `/api/tareas/?estado=pendiente` |
| Completar tarea | PATCH | `/api/tareas/{id}/` |

## Modelo Tarea

- `id`: integer
- `titulo`: string
- `curso`: string
- `fechaEntrega`: date ISO 8601
- `estado`: `pendiente | completada`

## Ejemplo de respuesta al consultar una tarea

```json
{
  "id": 1,
  "titulo": "Ensayo de historia",
  "curso": "Historia Universal",
  "fechaEntrega": "2026-10-05",
  "estado": "pendiente"
}
```

## Tarea no encontrada

Código HTTP: `404 Not Found`

```json
{
  "error": "No existe una tarea con ese id"
}
```

## Completar tarea

```http
PATCH /api/tareas/1/
Content-Type: application/json
```

```json
{
  "estado": "completada"
}
```

Se utiliza `PATCH` porque únicamente se modifica el campo `estado`.

## Breaking Change

Cambiar el nombre del campo `fechaEntrega` por `fecha_entrega` rompería el contrato, porque los clientes existentes que esperan `fechaEntrega` dejarían de encontrar ese dato.

