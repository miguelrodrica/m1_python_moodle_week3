def menu_inventory():
        while True:
            print("")
            print("\033[95m--- MENÚ INVENTARIO ---\033[0m")
            print("1. Agregar producto")
            print("2. Ver inventario")
            print("3. Buscar producto")
            print("4. Actualizar producto")
            print("5. Eliminar producto")
            print("6. Estadísticas")
            print("7. Guardar CSV")
            print("8. Cargar CSV")
            print("9. Salir")
            print("")
            try:
                menu_choice = int(input("Seleccione una opción: "))
                if menu_choice <= 0 or menu_choice > 9:
                        print("\033[91m¡ERROR!. Opción no contemplada en la lista. Intente de nuevo.\033[0m")
                        continue
                else:
                    break
            except ValueError:
                        print("\033[91m¡ERROR!. Debe ingresar un número entero. Intente de nuevo.\033[0m")
        return menu_choice

def add_product():
    """
    Esta función está hecha para agregar productos nuevos al inventario. Le solicita al usuario ingresar los datos (nombre, precio, cantidad), valida el formato de los mismos y finalmente retorna una lista que incluye un diccionario para cada producto.
    """
    inventory = []
    while True:
        try:
            quantity = int(input("¿Cuántos productos desea ingresar?: "))
            if quantity <= 0:
                print("\033[91m¡ERROR!. Ingrese un número positivo y diferente a 0.\033[0m")
                continue
            else:
                for i in range(quantity):
                    product = {}
                    print("")
                    print(f"\033[96mProducto #{i+1}\033[0m")
                    name_product = input("Nombre: ").lower()
                    product["name"] = name_product
                    while True:
                        try:
                            price_product = float(input("Precio: "))
                            if price_product <= 0:
                                print("\033[91m¡ERROR!. El precio debe ser mayor a $0.\033[0m")
                                continue
                            else:
                                product["price"] = price_product
                            break
                        except ValueError:
                            print("\033[91m¡ERROR!. Debe ingresar un número.\033[0m")
                    while True:
                        try:
                            quantity_product = int(input("Cantidad: "))
                            if quantity_product <= 0:
                                print("\033[91m¡ERROR!. La cantidad debe ser mayor a 0.\033[0m")
                                continue
                            else:
                                product["qty"] = quantity_product
                            break
                        except ValueError:
                            print("\033[91m¡ERROR!. Debe ingresar un número.\033[0m")
                    inventory.append(product)
            break
        except ValueError:
            print("\033[91m¡ERROR!. Debe ingresar un número entero.\033[0m")
    return inventory

def show_inventory(inventory):
    """
    Esta función se encargar imprimir el contenido total de inventario. Si este está vacío muestra un mensaje de advertencia.
    """
    if len(inventory) == 0:
        print("\033[93m¡El inventario está vacío!\033[0m")
    else:
        for product in inventory:
            print(f"\033[92mNombre: {product["name"]} | Precio: {product["price"]} | Cantidad: {product["qty"]}\033[0m")

def search_product(inventory):
    """
    Consultar la información de un producto en el diccionario. La validación se ejecuta por medio de un bucle For que busca el nombre del producto y si lo encuentra imprime la información correspondiente.
    """
    repeat = True
    while repeat:
        name_product = input("Escriba el nombre del producto a buscar: ").lower()
        for product in inventory:
            if product["name"] == name_product:
                print(f"\033[92mNombre: {product["name"]} | Precio: {product["price"]} | Cantidad: {product["qty"]}\033[0m")
                break
        repeat = False
        if product["name"] != name_product:
            print("\033[93mEl producto no existe en el inventario. Intente de nuevo\033[0m")
            print("")
            repeat = True

def update_product(inventory):
    """
    Función que actualiza la información de un producto, permite cambiar el dato del precio y la cantidad guardado en el inventario. Se le solicita al usuario la nueva información y esta se reemplaza en la posición original del diccionario.
    """
    repeat = True
    while repeat:
        name_product = input("Escriba el nombre del producto a actualizar: ").lower()
        for product in inventory:
            if product["name"] == name_product:
                new_price = float(input(f"Nuevo precio de {product["name"]}: "))
                new_qty = int(input(f"Nueva cantidad de {product["name"]}: "))

                product["price"] = new_price
                product["qty"] = new_qty

                print("\033[92mProducto actualizado correctamente.\033[0m")
                repeat = False
                break
            else:
                print("\033[93mEl producto no existe, intente nuevamente.\033[0m")
                continue
        

def remove_product(inventory):
    """
    Función para borrar un producto del inventario. Se usó el método .remove() para ejecutar la solicitud.
    """
    repeat = True
    while repeat:
        name_product = input("Escriba el nombre del producto a eliminar: ")
        for product in inventory:
            if name_product == product["name"]:
                inventory.remove(product)
                print(f"\033[92mSe eliminó el producto {product["name"]} del inventario\033[0m")
                break
        repeat = False
        if name_product != product["name"]:
            print("\033[93mEl producto no existe en el inventario. Intente de nuevo\033[0m")
            print("")
            repeat = True

def stats(inventory):
    all_qty = []
    all_total = []
    for product in inventory:
        product_qty = product["qty"]
        all_qty.append(product_qty)
        product_price = product["price"]
        total_product = product_price * product_qty
        all_total.append(total_product)
    #inventory[product]["price"]
    print(f"\033[92mEl total de unidades ingresadas es: {sum(all_qty)}\033[0m")
    print(f"\033[92mEl valor total del inventario es: {sum(all_total)}\033[0m")
    expensive_product = max(inventory, key=lambda p: p["price"])
    print(f"\033[92mEl producto más costoso es: {expensive_product["name"]}\033[0m")
    more_qty = max(inventory, key=lambda p: p["qty"])
    print(f"\033[92mEl producto con más stock es: {more_qty["name"]}\033[0m")
