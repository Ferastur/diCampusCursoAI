# 📄 Informe del Proyecto: Sistema de Gestión de Biblioteca

## 1. Arquitectura de Datos
El sistema utiliza una base de datos relacional SQLite con 4 tablas principales:
- `usuarios`: Almacena datos personales, teléfonos y fechas de penalización.
- `libros`: Contiene la metadata de los libros y el enlace (URL) a la imagen de portada.
- `prestamos`: Tabla pivote que gestiona la relación entre usuarios y libros, controlando estados y fechas.
- `configuracion`: Tabla global para definir parámetros como días máximos de préstamo.

## 2. Lógica de Negocio
Se han implementado restricciones de integridad:
- Un usuario no puede pedir libros si tiene una **penalización activa**.
- Se verifica el **stock disponible** antes de cada préstamo.
- Se limita el **número máximo de libros** por usuario según la configuración del administrador.

## 3. Innovación
La integración con la API de WhatsApp mediante URLs dinámicas permite una gestión de cobranza y avisos eficiente, reduciendo la tasa de libros perdidos. La carga de imágenes mediante `urllib` e `io` permite un catálogo visualmente atractivo sin necesidad de almacenar archivos pesados localmente.