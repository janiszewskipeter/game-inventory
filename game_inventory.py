import sys
import csv
added_items = {}
removed_items = {}
line = "_"*55
order = []
inventory = {'shotgun':2,'ak47':5, 'knife':8, 'pistol':1, 'uzi':5, 'ckm':1}


def main():
    print(line)
    choose = input("Welcome in th game inventory, what would You like to do: \n 1 - Add to inventory \n 2 - Remove from inventory \n 3 - Print by order \n 4 - Import inventory \n 5 - Export inventory \n 6 - Quit inventory \n Enter a number: \n")
    if choose == "1":
        add_to_inventory(inventory, added_items)
    elif choose == "2":
        remove_from_inventory(inventory, removed_items)
    elif choose == "3":
        print("Inventory by order")
        print(line)
        print_table(inventory, order)
    elif choose == "4":
        print("Import inventory")
    elif choose == "5":
        print("Export inventory")    
    elif choose == "6":
        sys.exit()


def display_inventory(inventory):
    print(line)
    for k, v in inventory.items():
        print("Weapon type: " ,k ,"|","ammo : ", v)
    print(line)
   

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
    order = input("What type of order would You like?\n No answer = no order \n desc - descending order \n asc -ascending order\n")
    if order == "":
        display_inventory(inventory)
    elif order == "asc":
        num = dict(sorted(inventory.items(), key=lambda x: x[1]))
        print(line)
        print("Ascending order of inventory")
        print(line)
        print("Item name  | count ")
        for k, v in num.items():
            print(k ,"      |", v)
        main()    
    else:
        num = dict(sorted(inventory.items(), key=lambda x: x[1], reverse=True))
        print("Descending order of inventory")
        for k, v in num.items():
            print("Weapon type: " ,k ,"|","ammo : ", v)  
        main()


def import_inventory(inventory, filename):
    """Import new inventory items from a CSV file."""
    pass


def export_inventory(inventory, filename):
    """Export the inventory into a CSV file."""

    pass



    
       

if __name__ == '__main__':
    main()