import csv
import os
field = ["name","price","qty"]

def save_csv(inventory):
    if len(inventory) == 0:
        print("\033[93mEl inventario está vacío, no se puede guardar\033[0m")
    else:
        escribir_header = not os.path.exists('m1_python_moodle_week3/inventario.csv') or os.path.getsize('m1_python_moodle_week3/inventario.csv') == 0
        with open('m1_python_moodle_week3/inventario.csv', 'a', newline='') as archivo:
            write_product = csv.DictWriter(archivo, fieldnames=field)
            if escribir_header:
                write_product.writeheader()
            write_product.writerows(inventory)
            print(f"\033[92mInventario guardado en {'m1_python_moodle_week3/inventario.csv'}\033[0m")

def load_csv():
    with open("m1_python_moodle_week3/inventario.csv", "r") as archivo:
        load_product = csv.DictReader(archivo, fieldnames=field)
        next(load_product)
        for fila in load_product:
            print(f"\033[92mNombre: {fila["name"]} | Precio: {fila["price"]} | Cantidad: {fila["qty"]}\033[0m")