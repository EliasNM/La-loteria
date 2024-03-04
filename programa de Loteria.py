import random

def generar_numeros_aleatorios(cantidad, rango_min, rango_max):
    #Genera una lista de 'cantidad' números aleatorios dentro del rango especificado.
    return [random.randint(rango_min, rango_max) for _ in range(cantidad)]

def comparar_numeros_elegidos_y_aleatorios(elegidos, aleatorios):
    #Compara los números elegidos por el usuario con los números generados aleatoriamente.
    aciertos = 0
    for num in elegidos:
        if num in aleatorios:
            aciertos += 1
    return aciertos

def jugar_loteria():
    #Función principal que permite al usuario jugar a la lotería.#
    print("¡Bienvenido a la lotería!")

    while True:
        try:
            cantidad_numeros = int(input("Ingrese la cantidad de números que desea jugar: "))
            rango_min = int(input("Ingrese el rango mínimo para los números: "))
            rango_max = int(input("Ingrese el rango máximo para los números: "))
            if rango_min >= rango_max:
                print("El rango mínimo debe ser menor que el rango máximo. Intente nuevamente.")
                continue

            numeros_elegidos = []
            for i in range(cantidad_numeros):
                numero = int(input(f"Ingrese el número {i+1}: "))
                numeros_elegidos.append(numero)

            numeros_aleatorios = generar_numeros_aleatorios(cantidad_numeros, rango_min, rango_max)
            print("Los números aleatorios son:", numeros_aleatorios)

            aciertos = comparar_numeros_elegidos_y_aleatorios(numeros_elegidos, numeros_aleatorios)
            print(f"¡Ha acertado {aciertos} números!")

            jugar_nuevamente = input("¿Desea jugar de nuevo? (si/no): ").lower()
            if jugar_nuevamente != 'si':
                print("Gracias por jugar. ¡Hasta luego!")
                break
        except ValueError:
            print("Por favor, ingrese números válidos.")

# Llamada a la función principal para iniciar el juego de la lotería
jugar_loteria()