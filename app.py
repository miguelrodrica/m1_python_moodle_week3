from servicios import *
from archivos import *

inventory = []

while True:
    menu_choice = menu_inventory()
    if menu_choice == 1:
        inventory = add_product()
        continue
    elif menu_choice == 2:
        show_inventory(inventory)
        continue
    elif menu_choice == 3:
        search_product(inventory)
        continue
    elif menu_choice == 4:
        update_product(inventory)
        continue
    elif menu_choice == 5:
        remove_product(inventory)
        continue
    elif menu_choice == 6:
        stats(inventory)
        continue
    elif menu_choice == 7:
        save_csv(inventory)
        continue
    elif menu_choice == 8:
        load_csv()
        continue
    else:
        print("\033[93m¡Bye!\033[0m")
        break
