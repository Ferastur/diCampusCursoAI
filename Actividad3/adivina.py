import random

def jugar_adivina_numero():
    puntuacion_total = 0
    partidas_jugadas = 0

    print("=======================================")
    print("  ¡Bienvenido a 'Adivina el número'!  ")
    print("=======================================")
    print("Instrucciones:")
    print("- Pensaré en un número del 1 al 100.")
    print("- Tienes exactamente 7 intentos para adivinarlo.")
    print("- Puntuación: 10 puntos por ganar + 2 puntos extra por cada intento sobrante.")

    while True:
        numero_secreto = random.randint(1, 100)
        intentos_maximos = 7
        partidas_jugadas += 1
        
        print(f"\n--- PARTIDA {partidas_jugadas} ---")
        print("Ya tengo mi número. ¡Empieza a adivinar!")

        # Bucle para los 7 intentos
        for intento_actual in range(1, intentos_maximos + 1):
            intentos_restantes = (intentos_maximos - intento_actual) + 1
            
            # Validación de entrada: nos aseguramos de que ingrese un número
            while True:
                try:
                    eleccion = int(input(f"\nIntento {intento_actual}/7 (Te quedan {intentos_restantes}). Ingresa un número: "))
                    break # Salimos del bucle de validación si es un número correcto
                except ValueError:
                    print("⚠️ Por favor, ingresa solo números enteros válidos.")

            # Comprobar la respuesta
            if eleccion == numero_secreto:
                puntos_obtenidos = 10 + (intentos_restantes * 2)
                puntuacion_total += puntos_obtenidos
                print(f"\n🎉 ¡CORRECTO! El número era el {numero_secreto}.")
                print(f"Has ganado {puntos_obtenidos} puntos en esta ronda.")
                break # Salimos del bucle de intentos porque ya adivinó
            
            elif eleccion < numero_secreto:
                print("➡️ Pista: El número secreto es **más alto**.")
            
            else:
                print("⬇️ Pista: El número secreto es **más bajo**.")

        # Este 'else' pertenece al 'for'. Se ejecuta SOLO si se acaban los intentos sin usar un 'break'
        else:
            print(f"\n💀 ¡Agotaste tus 7 intentos! El número secreto era el {numero_secreto}.")

        # Mostrar puntuación actual
        print(f"\n🏆 Puntuación Total: {puntuacion_total} puntos.")

        # Preguntar si quiere jugar de nuevo
        jugar_de_nuevo = input("\n¿Quieres jugar otra vez? (s/n): ").strip().lower()
        
        if jugar_de_nuevo != 's' and jugar_de_nuevo != 'si' and jugar_de_nuevo != 'sí':
            print("\n=======================================")
            print(f"¡Gracias por jugar! Tu puntuación final fue de {puntuacion_total} puntos en {partidas_jugadas} partidas.")
            print("=======================================\n")
            break # Salimos del bucle principal y termina el juego

# Ejecutar el juego
if __name__ == "__main__":
    jugar_adivina_numero()