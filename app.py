from services import add_product
from services import show_inventory
from services import search_product
from services import update_product
from services import remove_product

inventory = add_product()

show_inventory(inventory)
search_product(inventory)
update_product(inventory)
remove_product(inventory)
print(inventory)