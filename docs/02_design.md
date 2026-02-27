# Flujos Conversacionales y Arquitectura

## Flujos Conversacionales

El chatbot opera bajo un modelo basado en intenciones.  
Cada mensaje del usuario es procesado por Dialogflow y dirigido al flujo correspondiente en el backend.

### Flujo General

Inicio → Bienvenida → Identificación de intención → Respuesta específica →  
(Opcional) Registro de solicitud → Despedida

### Flujos Implementados

- **Bienvenida**  
  Presenta las capacidades principales del chatbot y las opciones disponibles.

- **Consultar horario**  
  Devuelve información general de horarios de atención mediante respuesta directa.

- **Requisitos de trámite**  
  Muestra un menú estructurado (vacunación, control prenatal, referencia).  
  Incluye validación en backend para mejorar precisión y reducir ambigüedad.

- **Registrar solicitud**  
  Flujo multi-turn que captura:
  - Nombre
  - Descripción
  - Medio de contacto (opcional)
  - Confirmación final  

  La información se almacena para seguimiento posterior.

- **Ayuda**  
  Orienta al usuario sobre las opciones disponibles.

- **Fallback**  
  Maneja mensajes no reconocidos y redirige a opciones válidas para mantener continuidad conversacional.

---

## Arquitectura de Implementación (Cloud)

La solución opera en un entorno desplegado en la nube.

### Componentes

- **Telegram**: canal de mensajería e interacción con el ciudadano.
- **Dialogflow**: identificación de intenciones y enrutamiento hacia el webhook.
- **Webhook desplegado en Render**: backend en entorno Cloud que procesa la lógica conversacional.
- **Gunicorn**: servidor WSGI utilizado para ejecutar la aplicación en producción.
- **Google Sheets**: almacenamiento estructurado de solicitudes registradas.

### Flujo de Integración

1. Usuario envía mensaje por Telegram.  
2. Dialogflow identifica la intención.  
3. Dialogflow invoca el webhook desplegado en Render.  
4. El backend procesa la lógica del flujo.  
5. Si aplica, se registra la solicitud en Google Sheets.  
6. Se devuelve la respuesta al usuario a través de Telegram.

---

## Principios de Diseño

- Modularidad
- Escalabilidad
- Mantenibilidad
- Despliegue en entorno Cloud
- Orientación al ciudadano
