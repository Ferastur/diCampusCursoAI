# --- Funciones de Operaciones ---
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    # Nota: En Python 3, la división '/' siempre devuelve un flotante. 
    # Si quieres que el resultado sea entero, se usa '//' (división entera).
    return a / b

def dividir_entera(a, b):
    return a // b

def calcular_modulo(a, b):
    return a % b

def potenciar(a, b):
    return a ** b

# --- Función de Validación (ACTUALIZADA A ENTEROS) ---
def obtener_numero(mensaje):
    """Asegura que la entrada sea un número entero y no texto o decimales."""
    while True:
        entrada = input(mensaje)
        try:
            # Cambiamos float(entrada) por int(entrada)
            return int(entrada)
        except ValueError:
            print("❌ Error: Entrada no válida. Por favor, introduce solo números ENTEROS (sin decimales).")

# --- Lógica Principal ---
def calculadora():
    print("--- Calculadora Modular (Solo Enteros) ---")
    print("Operadores: +, -, *, /, //, %, **")
    
    while True:
        # Obtención segura de números enteros
        num1 = obtener_numero("\nIntroduce el primer número entero: ")
        
        operador = input("Introduce el operador (+, -, *, /, //, %, **): ")
        
        num2 = obtener_numero("Introduce el segundo número entero: ")

        resultado = None

        try:
            if operador == '+':
                resultado = sumar(num1, num2)
            elif operador == '-':
                resultado = restar(num1, num2)
            elif operador == '*':
                resultado = multiplicar(num1, num2)
            elif operador == '/':
                resultado = dividir(num1, num2)
            elif operador == '//':
                resultado = dividir_entera(num1, num2)
            elif operador == '%':
                resultado = calcular_modulo(num1, num2)
            elif operador == '**':
                resultado = potenciar(num1, num2)
            else:
                print("⚠️ Operador no reconocido.")
                continue

            # Mostramos el resultado
            print(f"✅ Resultado: {num1} {operador} {num2} = {resultado}")

        except ZeroDivisionError:
            print("❌ Error: No se puede dividir por cero.")

        # Opción para salir
        continuar = input("\n¿Quieres realizar otra operación? (s/n): ").lower()
        if continuar != 's':
            print("¡Adiós!")
            break

if __name__ == "__main__":
    calculadora()