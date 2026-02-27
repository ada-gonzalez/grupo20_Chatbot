# Escenarios de Prueba – Webhook

## Endpoint

**Método:** POST  
**Ruta:** `/webhook`  
**Content-Type:** `application/json`

---

## 1. Consulta de requisitos de trámite

### Descripción
El usuario solicita información sobre los requisitos necesarios para iniciar un trámite.

### Request

```json
{
  "session": "test-requisitos-001",
  "queryResult": {
    "intent": {
      "displayName": "requisitos_tramite_inicio"
    },
    "queryText": "Necesito consultar requisitos para iniciar un trámite"
  }
}
```

### Comportamiento Esperado

- El sistema identifica el intent `requisitos_tramite_inicio`.
- Se devuelve un listado de trámites disponibles.
- Se solicita al usuario que seleccione un trámite por número o nombre.

### Respuesta Esperada (Ejemplo)

```json
{
  "fulfillmentText": "Claro. ¿Qué trámite deseas consultar?\n\n1. Control prenatal\n2. Vacunación\n3. Referencia\n\nPuedes responder con el número o el nombre del trámite."
}
```

---

## 2. Selección de trámite específico

### Descripción
El usuario selecciona un trámite específico después de recibir el listado de opciones.

### Request

```json
{
  "session": "test-requisitos-002",
  "queryResult": {
    "intent": {
      "displayName": "prueba"
    },
    "queryText": "control"
  }
}
```

### Comportamiento Esperado

- El sistema interpreta correctamente la selección del trámite.
- Se devuelven los requisitos correspondientes al trámite seleccionado.

### Respuesta Esperada (Ejemplo)

```json
{
  "fulfillmentText": "Para control prenatal se solicita DUI y prueba de embarazo positiva."
}
```

---

## 3. Inicio de registro de solicitud

### Descripción
El usuario inicia el proceso para registrar una nueva solicitud.

### Request

```json
{
  "session": "test-registro-001",
  "queryResult": {
    "intent": {
      "displayName": "registrar_solicitud_inicio"
    },
    "queryText": "Quiero registrar una solicitud"
  }
}
```

### Comportamiento Esperado

- El sistema identifica el intent `registrar_solicitud_inicio`.
- Se inicia el flujo de registro de solicitud.
- Se solicita el primer dato requerido (por ejemplo, nombre del solicitante).

### Respuesta Esperada (Ejemplo)

```json
{
  "fulfillmentText": "Con gusto. Para registrar tu solicitud necesito algunos datos.\n\n¿Cuál es tu nombre?"
}
```

---

## Validaciones Generales

- Todas las pruebas deben retornar **HTTP 200 OK**.
- El cuerpo de la respuesta debe estar en formato JSON.
- Para continuidad de flujo, se debe usar un intent diferente a **_inicio**.
- La respuesta debe incluir el campo `fulfillmentText`.
- El manejo de la `session` debe ser coherente dentro de cada escenario.
- No deben presentarse errores internos del servidor.
