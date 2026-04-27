# CLI Task Tracker - Python Core

Gestor de tareas de línea de comandos desarrollado en Python, con enfoque en la persistencia de datos, lógica de estados y trazabilidad temporal.

## Características

A diferencia de un Task Tracker convencional, este proyecto implementa:
- Persistencia con JSON: Los datos se almacenan y cargan automáticamente desde un archivo local.
- Ciclo CRUD Completo: Capacidad para Crear, Leer, Actualizar y Eliminar registros.
- Auditoría Temporal: Registro automatizado de fecha de creación (createdAt) y última modificación (updatedAt).
- Sistema de Filtrado: Visualización selectiva de tareas por estatus (ToDo, In Progress, Done).
- Gestión de IDs: Lógica para la asignación inteligente de identificadores únicos basados en el histórico de la lista.

## Tecnologías Usadas

- Python 3.x
- JSON (Manejo de archivos persistentes)
- Datetime (Gestión de sellos de tiempo)

## Estructura de Datos

Cada tarea se almacena como un objeto dentro de una lista JSON con el siguiente formato:

```json
{
    "Id": 1,
    "Descripcion": "Estudiar POO en Python",
    "Estatus": "ToDo",
    "createdAt": "2026-04-27 06:21:00",
    "updatedAt": "2026-04-27 07:45:12"
}