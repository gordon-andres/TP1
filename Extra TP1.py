# Programa básico de gestión de inventario

# Inicializar el inventario como un diccionario vacío
inventory = {}

def agregar_producto(name, quantity):
    if name in inventory:
        print(f"El producto '{name}' ya existe en el inventario.")
    else:
        inventory[name] = quantity
        print(f"Producto '{name}' agregado con cantidad {quantity}.")

def eliminar_producto(name):
    if name in inventory:
        del inventory[name]
        print(f"Producto '{name}' eliminado del inventario.")
    else:
        print(f"El producto '{name}' no existe en el inventario.")

def mostrar_inventario():
    if not inventory:
        print("El inventario está vacío.")
    else:
        print("Inventario actual:")
        for name, quantity in inventory.items():
            print(f"{name}: {quantity}")

def menu():
    while True:
        print("\nMenú de gestión de inventario:")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Mostrar inventario")
        print("4. Salir")

        option = input("Seleccione una opción (1-4): ")

        if option == '1':
            name = input("Ingrese el nombre del producto: ")
            quantity = int(input("Ingrese la cantidad inicial del producto: "))
            agregar_producto(name, quantity)
        elif option == '2':
            name = input("Ingrese el nombre del producto a eliminar: ")
            eliminar_producto(name)
        elif option == '3':
            mostrar_inventario()
        elif option == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

# Ejecutar el menú interactivo
menu()