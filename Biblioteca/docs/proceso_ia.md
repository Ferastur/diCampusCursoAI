1. Fase de Planificación con IA
Prompt enviado a la IA:
"Genera 5 historias de usuario para un sistema de gestión de biblioteca donde existan roles de Administrador y Usuario. Además, crea un diagrama de flujo en formato texto que describa el proceso de préstamo de un libro, teniendo en cuenta validaciones de stock y penalizaciones."
Respuesta de la IA:
Historias de Usuario:
Como Administrador, quiero poder dar de alta nuevos libros con su URL de portada para mantener el catálogo actualizado y visualmente atractivo.
Como Usuario, quiero buscar libros por título o autor y ver solo los que están disponibles para no perder tiempo con libros agotados.
Como Usuario, quiero solicitar el préstamo de un libro y que el sistema me asigne una fecha de devolución automática para saber cuándo debo entregarlo.
Como Administrador, quiero visualizar una lista de usuarios con libros fuera de plazo para poder enviarles un recordatorio por WhatsApp de forma rápida.
Como Administrador, quiero registrar la devolución de un libro para que el sistema calcule si hubo retraso y aplique una penalización de 7 días si es necesario.
Diagrama de Flujo del Proceso de Préstamo (Texto):
code
Text
INICIO
 └─> Usuario selecciona un libro del catálogo
 └─> ¿Hay stock disponible?
      ├─ NO: Mostrar mensaje "Libro no disponible" -> FIN
      └─ SÍ: Continuar
 └─> ¿Tiene el usuario una penalización activa?
      ├─ SÍ: Mostrar "Usuario bloqueado hasta [fecha]" -> FIN
      └─ NO: Continuar
 └─> ¿Ha superado el límite máximo de libros (3)?
      ├─ SÍ: Mostrar "Límite de préstamos alcanzado" -> FIN
      └─ NO: Continuar
 └─> REGISTRAR PRÉSTAMO
      ├─ Guardar ID Usuario e ID Libro
      ├─ Calcular Fecha Límite (Hoy + 15 días)
      ├─ Restar 1 al Stock del Libro
      └─ Mostrar "Préstamo Exitoso" con Fecha Límite
FIN

2. Cambios realizados por el alumno (Human-in-the-loop)
Tras recibir la propuesta inicial de la IA, he realizado los siguientes ajustes manuales para adaptar el sistema a las necesidades reales de Talento Solutions:
Refinamiento de la Penalización: La IA propuso una penalización genérica. Yo he especificado en el código que sea exactamente de 7 días naturales y que se aplique en el momento exacto en que el Administrador registra la devolución tardía.
Privacidad de Datos: He modificado la lógica de la "Ficha de Libro". Aunque la IA sugirió que todos vieran el historial, he restringido esa vista solo para Administradores, protegiendo la privacidad de los préstamos de los alumnos.
Integración de WhatsApp: La IA no incluyó el método de contacto. He añadido manualmente la generación de la URL wa.me utilizando el campo de teléfono del usuario para automatizar la gestión de mora.
Validación de Inputs: He añadido expresiones regulares (Regex) para validar que el email tenga un formato correcto y que la contraseña sea segura, algo que no estaba en el diseño inicial.

3. Reflexión sobre Automatización
Tareas que haría con automatización "normal" (Scripts/GitHub Actions):
Subida del código al repositorio y chequeo de sintaxis (Linting).
Copia de seguridad semanal de la base de datos biblioteca_v3.db.
Tareas que mejoraría con IA:
Recomendaciones: Un motor de IA que sugiera libros basados en el historial de lectura del usuario.
Chatbot: Un asistente que responda por WhatsApp si un libro está disponible sin que el usuario tenga que entrar en la aplicación.
Análisis de Datos: IA para predecir qué épocas del año hay más demanda de ciertos libros para ajustar el stock.

4. Prompt para Tests:
"Genera 3 tests unitarios en Python usando unittest para mi sistema de biblioteca. Deben probar el hashing de contraseñas, la lógica de sumar 7 días de penalización y la validación de formato de email con Regex."
Respuesta de la IA:
(La IA generó el código de arriba).
¿Qué he cambiado yo?
Contextualización: Adapté el test de penalización para que use el formato de fecha exacto (%Y-%m-%d) que utiliza mi base de datos SQLite, asegurando que la comparación no falle por culpa del formato de la hora.
Casos de prueba: Añadí una comprobación de longitud de caracteres (64) en el test de seguridad para garantizar que el algoritmo SHA-256 se está ejecutando correctamente y no otro más débil.


5. Automatización Tradicional vs. IA
En el desarrollo de este sistema de biblioteca, he identificado tareas que deben ser gestionadas por procesos deterministas (automatización normal) y otras que pueden ser potenciadas mediante modelos de lenguaje o aprendizaje automático (IA).
A. Automatización "Normal" (Scripts y GitHub Actions)
Estas tareas son mecánicas, repetitivas y requieren 100% de precisión lógica. No necesitan "pensar", solo ejecutar.
Integración Continua (CI): Configurar un GitHub Action que ejecute automáticamente mis 3 tests unitarios cada vez que subo código (git push). Si un test falla, el código no se marca como válido.
Backups de Base de Datos: Un script programado (cron job) que realice una copia de seguridad del archivo biblioteca_v3.db cada 24 horas para evitar pérdida de datos.
Formateo de Código: Uso de herramientas como Black o Flake8 en un script para asegurar que todo el código Python siga las reglas de estilo PEP8 de forma automática.
Despliegue de la Landing Page: Automatizar que cualquier cambio en index.html se publique instantáneamente en GitHub Pages.
B. Tareas mejoradas con Inteligencia Artificial
Estas tareas involucran datos no estructurados, predicciones o lenguaje natural, donde la IA aporta un valor cognitivo.
Búsqueda Semántica de Libros: En lugar de buscar solo por "Título exacto", usar IA (Embeddings) para que el usuario pueda buscar por conceptos. Ejemplo: Buscar "libros sobre la tristeza" y que la IA encuentre "La metamorfosis" de Kafka aunque la palabra "tristeza" no esté en el título.
Asistente de Recomendación: Implementar un motor de recomendación que analice los préstamos previos del alumno y diga: "Ya que leíste 'El Quijote', te sugiero 'La Galatea' de Cervantes".
Análisis Predictivo de Mora: Una IA que analice el comportamiento histórico de los alumnos y alerte al administrador sobre quién tiene más probabilidades de no devolver un libro a tiempo, permitiendo una gestión preventiva.
Generación de Resúmenes: Utilizar un LLM (como GPT o Gemini) para generar automáticamente resúmenes cortos de los libros a partir de su ISBN o título, enriqueciendo la ficha del libro sin trabajo manual.
Auditoría de Seguridad: Usar IA para analizar el código fuente en busca de vulnerabilidades (como inyecciones SQL que se nos hayan pasado) antes de pasar a producción.

=========================================================================================================================================

Resumen Final.

Código generado por IA : 90%
Código escrito o modificado por mi : 10%

IA Utilizada : Gemini 3 Flash Preview en AI Studio de Google.

