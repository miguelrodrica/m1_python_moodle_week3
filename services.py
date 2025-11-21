def add_product():
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
    if len(inventory) == 0:
        print("\033[93m¡El inventario está vacío!\033[0m")
    else:
        for product in inventory:
            print(f"\033[92mNombre: {product["name"]} | Precio: {product["price"]} | Cantidad: {product["qty"]}\033[0m")

def search_product(inventory):
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
                break
        repeat = False
        if product["name"] != name_product:
            print("\033[93mEl producto no existe en el inventario. Intente de nuevo\033[0m")
            print("")
            repeat = True

def remove_product(inventory):
    repeat = True
    while repeat:
        name_product = input("Escriba el nombre del producto a eliminar: ")
        for product in inventory:
            if name_product == product["name"]:
                inventory.remove(product)
                print(f"Se eliminó el producto {product["name"]} del inventario")
                break
        repeat = False
        if name_product != product["name"]:
            print("\033[93mEl producto no existe en el inventario. Intente de nuevo\033[0m")
            print("")
            repeat = True