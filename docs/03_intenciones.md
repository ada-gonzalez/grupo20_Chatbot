#Definir intenciones, ejemplos 
de frases de usuario, 
respuestas base y mensajes 
de error/fallback.

# Catálogo de Intenciones y Respuestas  
**Chatbot Asistente CSDC – Versión Lite**

Este documento define las intenciones principales del chatbot, ejemplos de frases de usuario y las respuestas base del sistema.  
Las intenciones están diseñadas para ser implementadas mediante flujos guiados y, en fases posteriores, mediante plataformas de interpretación de lenguaje natural como Dialogflow.

---

## 1. Intención: bienvenida

**Descripción:**  
Gestiona el inicio de la conversación y presenta las opciones principales del chatbot.

**Ejemplos de frases del usuario:**
- Hola  
- Buenos días  
- Buenas  
- Hola bot  
- Iniciar conversación  

**Respuesta base del chatbot:**
> ¡Hola! 👋  
> Bienvenido al asistente virtual del Centro de Servicios Digitales al Ciudadano (CSDC).  
> Puedo ayudarte con información sobre horarios de atención, requisitos de trámites o registrar una solicitud.  
> ¿En qué puedo ayudarte hoy?

---

## 2. Intención: consultar_horario

**Descripción:**  
Permite al ciudadano consultar los horarios de atención de las clínicas comunales.

**Ejemplos de frases del usuario:**
- ¿Cuál es el horario de atención?  
- ¿A qué hora atienden?  
- Horarios de la clínica  
- ¿Qué días atienden?  

**Respuesta base del chatbot:**
> El horario de atención de las clínicas comunales es de **lunes a viernes, de 7:00 a.m. a 3:00 p.m.**  
> Te recomendamos verificar posibles cambios en días festivos a través de los canales oficiales.

---

## 3. Intención: requisitos_tramite

**Descripción:**  
Brinda información sobre los requisitos necesarios para realizar trámites de salud específicos.

**Ejemplos de frases del usuario:**
- ¿Qué requisitos necesito para vacunarme?  
- Requisitos para control prenatal  
- ¿Qué documentos piden para una referencia médica?  

**Respuesta base del chatbot:**
> Para realizar este trámite es necesario presentar los documentos requeridos según el servicio solicitado.  
> Generalmente se solicita documento de identificación y, en algunos casos, referencia médica.  
> Si deseas información más específica, indícanos el trámite que deseas realizar.

---

## 4. Intención: registrar_solicitud

**Descripción:**  
Permite registrar una solicitud ciudadana básica cuando la consulta no puede resolverse automáticamente.

**Ejemplos de frases del usuario:**
- Quiero registrar una solicitud  
- Necesito hablar con un agente  
- Mi caso es diferente  

**Respuesta base del chatbot:**
> Para poder registrar tu solicitud, por favor indícame tu **nombre** y una breve descripción de tu consulta.  
> Esta información será utilizada para dar seguimiento a tu caso por los canales oficiales del CSDC.

---

## 5. Intención: ayuda

**Descripción:**  
Muestra al ciudadano las opciones disponibles y orienta sobre el uso del chatbot.

**Ejemplos de frases del usuario:**
- Ayuda  
- ¿Qué puedo hacer aquí?  
- Opciones  

**Respuesta base del chatbot:**
> Puedo ayudarte con las siguientes opciones:  
> • Consultar horarios de atención  
> • Conocer requisitos de trámites  
> • Registrar una solicitud  

---

## 6. Intención: fallback

**Descripción:**  
Gestiona mensajes que el chatbot no logra interpretar correctamente.

**Ejemplos de frases del usuario:**
- asdfgh  
- ???  
- (mensaje fuera de contexto)  

**Respuesta base del chatbot:**
> Lo siento, no logré entender tu consulta 
> Puedes preguntar por horarios de atención, requisitos de trámites o escribir *ayuda* para ver las opciones disponibles.

---

## 7. Intención: despedida

**Descripción:**  
Finaliza la conversación de forma cordial.

**Ejemplos de frases del usuario:**
- Gracias  
- Eso es todo  
- Adiós  

**Respuesta base del chatbot:**
> ¡Gracias por utilizar el asistente virtual del CSDC! 
> Si necesitas más información, no dudes en volver a escribirnos.

