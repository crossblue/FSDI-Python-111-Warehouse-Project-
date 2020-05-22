import os

def menu():
    print("\n\n")
    print("-" * 30)
    print("Warehouse Control")
    print("-" * 30)

    print(" [1] Register items")
    print(" [2] Display Catalog")
    print(" [3] Display out of Stock Items")
    print(" [4] Update item stock")
    print(" [5] Calculate stock value")
    print(" [6] Remove item from the menu")
    print(" [7] Register a Sale")
    print(" [8] Remove item from Catalog")
    print(" [9] Sort by Categories")

    print(" [x] Exit ")


def header(title):
    clear()
    print("-" * 70)
    print(" " + title)
    print("-" * 70)



def clear():
   return os.system('cls' if os.name == 'nt' else 'clear')


