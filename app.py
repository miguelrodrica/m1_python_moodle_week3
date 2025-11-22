from services import menu_inventory
from services import add_product
from services import show_inventory
from services import search_product
from services import update_product
from services import remove_product
from services import stats

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

    else:
        print("\033[93m¡Bye!\033[0m")
        break
