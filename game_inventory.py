
#git firts commmit
added_items = {}
removed_items = {}
inventory = {'shotgun':1,'ak47':1, 'knife':1, 'pistol':1}



def display_inventory(inventory):
    for k, v in inventory.items():
        print("Weapon type: " ,k ,"|","ammo : ", v)
    
   

def add_to_inventory(inventory, added_items):
    added_items = input("Please add a weapon or enter No to main menu :")
    if added_items == "no":
        main()
    elif added_items not in inventory.keys():
        inventory.setdefault(added_items, 1 )
    elif added_items in inventory.keys():
        inventory[added_items] += 1
    display_inventory(inventory)
    add_to_inventory(inventory, added_items)

def remove_from_inventory(inventory, removed_items):
    display_inventory(inventory)
    removed_items = input("Which weapon would you like to remove or no to go to main menu?")
    if removed_items == "No":
        main()
    elif removed_items in inventory.keys():
        del inventory[removed_items]
        remove_from_inventory(inventory, removed_items)
    elif removed_items not in inventory.keys():
        print("No such weapon so far") 
        main()  
def print_table(inventory, order):
    pass
    

def import_inventory(inventory, filename):
    """Import new inventory items from a CSV file."""

    pass


def export_inventory(inventory, filename):
    """Export the inventory into a CSV file."""

    pass

def main():
    print('-'*55)
    choose = input("Welcome in th game inventory, what would You like to do: \n 1 - Add to inventory \n 2 - Remove from inventory \n 3 - XXXX \n 4 - XXX \n 5 - Quit inventory \n Enter a number:")
    if choose == "1":
        add_to_inventory(inventory, added_items)
    elif choose == "2":
        remove_from_inventory(inventory, removed_items)
    elif choose == "3":
          

if __name__ == '__main__':
    main()
    display_inventory(inventory)
    add_to_inventory(inventory, added_items)