# Lista para agregar productos
productos = []

# Función muestra menú
def mostrar_menu():
    print("\n" + "*" * 30)
    print("--- Sistema de Inventario ---")
    print("1. Agregar producto")
    print("2. Visualizar productos")
    print("3. Salir del sistema")
    print("*" * 30)

# Función agrega productos
def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    
    # Valida que cantidad sea un int < 0
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad del producto: "))
            if cantidad >= 0:
                break
            else:
                print("Por favor ingrese una cantidad válida (número positivo).")
        except ValueError:
            print("Entrada no válida. Por favor ingrese un número entero.")

    productos.append([nombre, cantidad])
    print("Producto agregado con éxito.")

# Función visualiza productos
def visualizar_producto():
    if len(productos) == 0:
        # print("\n No hay productos agregados aún. \n")
        print("No hay productos registrados.")
    else:
        print("\n --- Productos registrados ---")
        indice = 1  # Inicia en índice en 1
        for producto in productos:
            print(f"Producto {indice}: Nombre: {producto[0]}, Cantidad: {producto[1]}")
            indice += 1
        # otra alternativa para eliminar la variable indice podría ser:
        # for indice, producto in enumerate(productos, start=1):

# Función principal para el sistema de inventario
def main():
    while True:
        mostrar_menu()
        
        # Validar que la opción ingresada sea un número entero entre 1 y 3
        try:
            opcion = int(input("\nSeleccione una opción: "))
        except ValueError:
            print("Opción no válida. Por favor ingrese un número entre 1 y 3.")
            continue

        if opcion == 1:
            agregar_producto()
        elif opcion == 2:
            visualizar_producto()
        elif opcion == 3:
            print("\nSaliendo del sistema\n")
            break
        else:
            print("Opción no válida. Por favor seleccione una opción correcta.")

# Ejecución de la función main()
if __name__ == "__main__":
    main()
