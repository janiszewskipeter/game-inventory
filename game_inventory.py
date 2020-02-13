
#git firts commmit
added_items = {}
inventory = {'shotgun':1,'ak47':1, 'knife':1, 'pistol':1}

def main():
    print('-'*55)
    choosen_path = input("Welcome in th game inventory, what would You like to do: \n 1 - Add to inventory \n 2 - Remove from inventory \n 3 - XXXX \n 4 - XXX \n 5 - Quit inventory \n")
    
def choosen_path():    
    if input == 1:
        add_to_inventory(inventory, added_items)
    elif input == 2:
        print("remove")


def display_inventory(inventory):
    for key, value in inventory.items():
        print("Weapon type:", key,"|","ammo :", value)
    
   

def add_to_inventory(inventory, added_items):
    added_items = input("Please add a weapon or enter N to main menu :" )
    if added_items not in inventory.keys():
        inventory.setdefault(added_items, 1 )
    elif added_items in inventory.keys():
        inventory[added_items] += 1
    display_inventory(inventory)
    add_to_inventory(inventory, added_items)

def remove_from_inventory(inventory, removed_items):
    """Remove from the inventory dictionary a list of items from removed_items."""
    pass


def print_table(inventory, order):
    """
    Display the contents of the inventory in an ordered, well-organized table with
    each column right-aligned.
    """

    pass


def import_inventory(inventory, filename):
    """Import new inventory items from a CSV file."""

    pass


def export_inventory(inventory, filename):
    """Export the inventory into a CSV file."""

    pass

if __name__ == '__main__':
    main()
    display_inventory(inventory)
    add_to_inventory(inventory, added_items)