# Flujos Conversacionales y Arquitectura

## Flujos Conversacionales

El chatbot opera bajo un modelo basado en intenciones, donde cada mensaje del usuario es analizado y dirigido a un flujo específico.

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
  Incluye validación en backend para reducir ambigüedad en la selección.

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
  Maneja mensajes no reconocidos y redirige a opciones válidas para evitar ruptura de la conversación.

---

## Arquitectura de Implementación

La solución se compone de los siguientes elementos:

- **Telegram**: canal de comunicación con el ciudadano.
- **Dialogflow**: identificación de intención y enrutamiento.
- **Webhook (Flask - Python)**: lógica conversacional y manejo de flujos multi-turn.
- **Google Sheets**: almacenamiento estructurado de solicitudes.
- **Ngrok (fase de desarrollo)**: exposición temporal del webhook local.

### Principios de Diseño

- Modularidad
- Escalabilidad
- Mantenibilidad
- Disponibilidad
- Orientación al ciudadano

---

## Integraciones Clave

1. Canal de comunicación ↔ Plataforma conversacional  
2. Motor de intenciones ↔ Backend  
3. Backend ↔ Sistema de registro (Google Sheets)

Estas integraciones permiten mantener continuidad del servicio, trazabilidad de solicitudes y reducción de carga operativa humana.
