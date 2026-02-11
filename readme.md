# 🧮 Suite de Calculadoras en Python

Este proyecto es una solución integral que incluye una calculadora modular por consola, una calculadora científica con interfaz gráfica (GUI) y un sistema automatizado de pruebas unitarias.

---

## 📂 Análisis Detallado de Funciones

A continuación se detalla el propósito de cada función dentro de los archivos del proyecto:

### 1. `calculadora.py` (Lógica Base)
Este archivo contiene el motor aritmético y la lógica de consola.

*   **`sumar(a, b)`**: Retorna la suma de dos números.
*   **`restar(a, b)`**: Retorna la diferencia entre el primer y el segundo número.
*   **`multiplicar(a, b)`**: Retorna el producto de dos números.
*   **`dividir(a, b)`**: Retorna el cociente flotante. Gestiona decimales.
*   **`dividir_entera(a, b)`**: Retorna el cociente descartando los decimales (suelo de la división).
*   **`calcular_modulo(a, b)`**: Retorna el resto de una división entera.
*   **`potenciar(a, b)`**: Eleva el primer número a la potencia del segundo.
*   **`obtener_numero(mensaje)`**: **Función de validación.** Utiliza un bucle infinito que solo se rompe cuando el usuario introduce un número válido. Captura el error si el usuario intenta ingresar texto.
*   **`calculadora()`**: Función principal que gestiona el menú, solicita los operadores y decide qué función aritmética llamar basándose en la entrada del usuario.

### 2. `cientifica.py` (Interfaz Gráfica)
Contiene la clase `CalculadoraCientifica` que construye la aplicación visual.

*   **`__init__(self, root)`**: Constructor de la interfaz. Configura la ventana, crea la variable de pantalla y genera la cuadrícula de botones (0-9, operadores y funciones científicas).
*   **`click_boton(self, valor)`**: El manejador de eventos principal. Determina si el botón pulsado es un número, una operación especial (C, DEL, =) o una función científica, y actúa en consecuencia.
*   **`insertar_funcion(self, nombre_func)`**: Toma el valor actual de la pantalla y lo envuelve en una función de la librería `math` (ej: convierte `45` en `math.sin(math.radians(45))`).
*   **`actualizar_pantalla(self, texto)`**: Método de seguridad. Cambia el estado de la pantalla de `readonly` a `normal` para poder escribir el nuevo resultado y lo vuelve a bloquear inmediatamente.
*   **`calcular(self)`**: Extrae el string de la pantalla y lo procesa con `eval()`. Utiliza un diccionario restringido para que solo se puedan ejecutar funciones matemáticas seguras.

### 3. `test_calculadora.py` (Pruebas de Calidad)
Script diseñado para asegurar que los cálculos sean correctos.

*   **`ejecutar_tests()`**: Ejecuta una serie de comandos `assert`. Compara el resultado real de las funciones de `calculadora.py` con un resultado esperado conocido. Si una función falla (por ejemplo, si la suma devuelve un valor incorrecto), el script informa exactamente en qué punto ocurrió el error.

---

## 🚀 Instalación y Uso

### Requisitos
- **Python 3.x** instalado.
- Los tres archivos deben estar en la misma carpeta para que las importaciones funcionen correctamente.

### Ejecución
1.  **Calculadora de Consola:** `python calculadora.py`
2.  **Calculadora Científica:** `python cientifica.py`
3.  **Pasar los Tests:** `python test_calculadora.py`

---

## ⚙️ Características Destacadas

1.  **Protección de Inputs:** En la versión de consola, el programa no se detiene si escribes letras; simplemente te avisa y te pide el número de nuevo.
2.  **Interfaz Bloqueada:** En la versión científica, el teclado está deshabilitado para el campo de texto, obligando a usar los botones para garantizar que la sintaxis matemática sea correcta.
3.  **Modularidad:** Las funciones matemáticas están separadas de la interfaz, lo que permite que puedan ser reutilizadas en otros proyectos o probadas de forma independiente.

---
**Desarrollado con Python 3** 🐍