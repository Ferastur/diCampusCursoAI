🧮 Calculadora Modular Python
Una calculadora sencilla basada en consola escrita en Python que permite realizar operaciones aritméticas básicas y avanzadas con validación de datos de entrada y una batería de pruebas automatizada.
🚀 Características
Operaciones soportadas:
Suma (+)
Resta (-)
Multiplicación (*)
División decimal (/)
División entera (//)
Módulo / Resto (%)
Potencia (**)
Validación de entradas: El sistema asegura que el usuario solo introduzca números enteros para evitar errores en tiempo de ejecución.
Manejo de errores: Gestión de excepciones como la división por cero.
Pruebas unitarias: Incluye un script independiente para verificar que todas las funciones matemáticas retornen los valores esperados.
📁 Estructura del Proyecto
Para que el sistema de importación de los tests funcione correctamente, se recomienda la siguiente estructura de carpetas:
code
Text
nombre-del-proyecto/
│
├── src/
│   └── app.py          # Lógica principal y calculadora
│
└── tests/
    └── test.py         # Batería de pruebas unitarias
🛠️ Instalación y Requisitos
Requisitos: Tener instalado Python 3.x.
Clonar o descargar: Copia los archivos en tu máquina local respetando la estructura de carpetas mencionada arriba.
💻 Uso
Para ejecutar la calculadora, sitúate en la raíz del proyecto y lanza el siguiente comando:
code
Bash
python src/app.py
Ejemplo de uso:
Introduce el primer número (ej. 10).
Elige un operador (ej. **).
Introduce el segundo número (ej. 2).
El resultado será 100.
🧪 Pruebas (Testing)
El proyecto incluye un archivo test.py que verifica la integridad de las funciones matemáticas. Para ejecutar los tests, sitúate en la carpeta tests/ o ejecuta desde la raíz:
code
Bash
python tests/test.py
Si todo es correcto, verás un mensaje confirmando que todas las funciones pasaron las pruebas:
✅ Función sumar: PASÓ ... 🎉 ¡Todos los tests han pasado con éxito!
📝 Notas del Código
Validación de Enteros: La función obtener_numero() ha sido diseñada específicamente para rechazar cadenas de texto y números decimales, garantizando que la lógica trabaje con int.
Modularidad: Las funciones matemáticas están separadas de la interfaz de usuario (CLI), lo que facilita su reutilización en otros módulos o proyectos.