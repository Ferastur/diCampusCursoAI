# Importamos las funciones del archivo anterior
# Nota: Asegúrate de que tu archivo de calculadora se llame 'calculadora.py'
from calculadora import (
    sumar, restar, multiplicar, dividir, 
    dividir_entera, calcular_modulo, potenciar
)

def ejecutar_tests():
    print("🧪 Iniciando batería de pruebas...")

    try:
        # Test Suma
        assert sumar(5, 3) == 8, "Error en sumar(5, 3)"
        assert sumar(-1, 1) == 0, "Error en sumar(-1, 1)"
        print("✅ Función sumar: PASÓ")

        # Test Resta
        assert restar(10, 5) == 5, "Error en restar(10, 5)"
        assert restar(5, 10) == -5, "Error en restar(5, 10)"
        print("✅ Función restar: PASÓ")

        # Test Multiplicación
        assert multiplicar(3, 4) == 12, "Error en multiplicar(3, 4)"
        assert multiplicar(5, 0) == 0, "Error en multiplicar(5, 0)"
        print("✅ Función multiplicar: PASÓ")

        # Test División
        assert dividir(10, 2) == 5.0, "Error en dividir(10, 2)"
        assert dividir(5, 2) == 2.5, "Error en dividir(5, 2)"
        print("✅ Función dividir: PASÓ")

        # Test División Entera
        assert dividir_entera(10, 3) == 3, "Error en dividir_entera(10, 3)"
        assert dividir_entera(20, 5) == 4, "Error en dividir_entera(20, 5)"
        print("✅ Función dividir_entera: PASÓ")

        # Test Módulo
        assert calcular_modulo(10, 3) == 1, "Error en calcular_modulo(10, 3)"
        assert calcular_modulo(20, 5) == 0, "Error en calcular_modulo(20, 5)"
        print("✅ Función calcular_modulo: PASÓ")

        # Test Potencia
        assert potenciar(2, 3) == 8, "Error en potenciar(2, 3)"
        assert potenciar(5, 0) == 1, "Error en potenciar(5, 0)"
        print("✅ Función potenciar: PASÓ")

        print("\n🎉 ¡Todos los tests han pasado con éxito!")

    except AssertionError as e:
        print(f"\n❌ FAILED: {e}")
    except Exception as e:
        print(f"\n⚠️ Ocurrió un error inesperado durante los tests: {e}")

if __name__ == "__main__":
    ejecutar_tests()