import math

# --- Funciones de Operaciones ---
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def dividir_entera(a, b):
    return a // b

def calcular_modulo(a, b):
    return a % b

# 1. Función potencia
def potencia(base, exponente):
    return base ** exponente

# 2. Función raíz cuadrada (con manejo de negativos en la lógica)
def raiz_cuadrada(numero):
    if numero < 0:
        # Levantamos un error de valor que luego capturaremos con el try-except
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo en los números reales.")
    return math.sqrt(numero)

# 3. Función calcular porcentaje
def calcular_porcentaje(porcentaje, total):
    return (porcentaje * total) / 100

# --- Función de Validación ---
def obtener_numero(mensaje):
    """Asegura que la entrada sea un número (permite decimales)."""
    while True:
        entrada = input(mensaje)
        try:
            # Cambiamos a float para soportar operaciones más complejas como raíces o porcentajes
            return float(entrada)
        except ValueError:
            print("❌ Error: Entrada no válida. Por favor, introduce un número válido.")

def mostrar_menu():
    """Imprime las opciones disponibles en pantalla."""
    print("\n" + "="*35)
    print("      CALCULADORA INTERACTIVA")
    print("="*35)
    print("1. Sumar (+)")
    print("2. Restar (-)")
    print("3. Multiplicar (*)")
    print("4. Dividir (/)")
    print("5. División Entera (//)")
    print("6. Módulo (%)")
    print("7. Potencia (base^exponente)")
    print("8. Raíz Cuadrada (√)")
    print("9. Calcular Porcentaje (%)")
    print("0. Salir")
    print("="*35)

# --- Lógica Principal ---
def calculadora():
    while True:
        # 4. Menú interactivo
        mostrar_menu()
        opcion = input("Elige una operación (0-9): ")

        if opcion == '0':
            print("¡Gracias por usar la calculadora! Adiós. 👋")
            break

        if opcion not in [str(i) for i in range(1, 10)]:
            print("⚠️ Opción no válida. Por favor, elige un número del 0 al 9.")
            continue

        # 5. Manejo de errores centralizado
        try:
            # La raíz cuadrada solo necesita un número
            if opcion == '8':
                num = obtener_numero("Introduce el número para calcular su raíz: ")
                resultado = raiz_cuadrada(num)
                print(f"\n✅ Resultado: √{num} = {resultado}")
            
            # El resto de operaciones requieren dos números
            else:
                if opcion == '9':
                    num1 = obtener_numero("Introduce el porcentaje a calcular (ej. 15 para 15%): ")
                    num2 = obtener_numero("Introduce el valor total: ")
                elif opcion == '7':
                    num1 = obtener_numero("Introduce el número base: ")
                    num2 = obtener_numero("Introduce el exponente: ")
                else:
                    num1 = obtener_numero("Introduce el primer número: ")
                    num2 = obtener_numero("Introduce el segundo número: ")

                # Evaluamos la opción elegida
                if opcion == '1':
                    print(f"\n✅ Resultado: {num1} + {num2} = {sumar(num1, num2)}")
                elif opcion == '2':
                    print(f"\n✅ Resultado: {num1} - {num2} = {restar(num1, num2)}")
                elif opcion == '3':
                    print(f"\n✅ Resultado: {num1} * {num2} = {multiplicar(num1, num2)}")
                elif opcion == '4':
                    print(f"\n✅ Resultado: {num1} / {num2} = {dividir(num1, num2)}")
                elif opcion == '5':
                    print(f"\n✅ Resultado: {num1} // {num2} = {dividir_entera(num1, num2)}")
                elif opcion == '6':
                    print(f"\n✅ Resultado: {num1} % {num2} = {calcular_modulo(num1, num2)}")
                elif opcion == '7':
                    print(f"\n✅ Resultado: {num1} elevado a {num2} = {potencia(num1, num2)}")
                elif opcion == '9':
                    print(f"\n✅ Resultado: El {num1}% de {num2} es = {calcular_porcentaje(num1, num2)}")

        # Captura específica para división por cero
        except ZeroDivisionError:
            print("\n❌ Error matemático: ¡No se puede dividir por cero!")
        
        # Captura específica para nuestros errores de valores (como la raíz negativa)
        except ValueError as e:
            print(f"\n❌ Error de valor: {e}")
        
        # Captura de cualquier otro error imprevisto (buena práctica)
        except Exception as e:
            print(f"\n❌ Ha ocurrido un error inesperado: {e}")

        # Pequeña pausa opcional antes de volver al menú
        input("\nPresiona 'Enter' para continuar...")

if __name__ == "__main__":
    calculadora()