n1: float
n2: float
opcion: str

def sumar(a: int, b: int):
    return a + b

def multiplicar(a: int, b: int):
    return a * b

def mostrar_menu():
    opcion = 0
    while opcion != 3:
        print("\n--- MENÚ DE OPCIONES ---")
        print("1. Sumar dos números")
        print("2. Multiplicar dos números")
        print("3. Salir")
        
        opcion = input("Selecciona una opción (1-3): ")

        match opcion:
            case '1':
                n1 = float(input("Introduce el primer número: "))
                n2 = float(input("Introduce el segundo número: "))
                print(f"El resultado de la suma es: {sumar(n1, n2)}")

            case '2':
                n1 = float(input("Introduce el primer número: "))
                n2 = float(input("Introduce el segundo número: "))
                print(f"El resultado de la multiplicación es: {multiplicar(n1, n2)}")

            case '3':
                print("Saliendo del programa... ¡Hasta luego!")
                break

            case _:
                print("Opción no válida. Por favor, intenta de nuevo.")
                       

if __name__ == "__main__":
    mostrar_menu()