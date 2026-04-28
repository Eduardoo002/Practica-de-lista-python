numeros = []

while True:
    print("\n--- MENÚ ---")
    print("1. Agregar número")
    print("2. Mostrar lista")
    print("3. Mostrar cantidad de números")
    print("4. Modificar un número por índice")
    print("5. Eliminar un número por índice")
    print("6. Mostrar suma y número mayor")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        num = int(input("Ingrese un número: "))
        numeros.append(num)
        print("Número agregado.")

    elif opcion == "2":
        print("Lista:", numeros)

    elif opcion == "3":
        print("Cantidad de números:", len(numeros))

    elif opcion == "4":
        if len(numeros) == 0:
            print("La lista está vacía.")
        else:
            indice = int(input("Ingrese el índice a modificar: "))
            if 0 <= indice < len(numeros):
                nuevo = int(input("Ingrese el nuevo número: "))
                numeros[indice] = nuevo
                print("Número modificado.")
            else:
                print("Índice inválido.")

    elif opcion == "5":
        if len(numeros) == 0:
            print("La lista está vacía.")
        else:
            indice = int(input("Ingrese el índice a eliminar: "))
            if 0 <= indice < len(numeros):
                numeros.pop(indice)
                print("Número eliminado.")
            else:
                print("Índice inválido.")

    elif opcion == "6":
        if len(numeros) == 0:
            print("La lista está vacía.")
        else:
            suma = sum(numeros)
            mayor = max(numeros)
            print("Suma total:", suma)
            print("Número mayor:", mayor)

    elif opcion == "7":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción no válida.")