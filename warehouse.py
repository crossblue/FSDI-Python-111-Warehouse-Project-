from menu import menu, clear, header
from item import Item
import pickle
import datetime



"""
Program: Wherehouse management system
Functionality:
        - Repeat menu
        - Register items to the catalog
            id (auto generated)
            title
            category
            price
            stock
        - Display Catalog
        - Display items with no stock (out of stock)

        - Saving / retrieving data to/from file
        
        - Update the stock of an item
           - show the list of items
           - ask the user to choose the id
           - ask the user for the new stock value
           - find the item with selected id
           - update the stock  
           - save changes

        - Print the total valus of the (sum(price * stock))

        - Remove an item from the Catalog

        - Register a Sale
            - show the list of items
            - ask the user to choose an id
            - ask the user to provide the qnty
            - update the stock

        - Have a log events
            - file name for logs
            - a list for the log entries (list of string)
            - add_log_event function that receives an string
            - save_log
            - read_log
            - update existing functions to register log enteries

        - Display the log of events

        - Display list of categories (show unique categories)
"""

# global vars
 
catalog = []
log = []
unique_categories = []
last_id = 0
data_file = 'warehouse.data'
log_file = 'logs.data'





def save_catalog():
    global data_file
    writer = open(data_file, "wb")# create file (overwirte if file exists), and open it to Write Binary
    pickle.dump(catalog, writer) # dump catalog data into the writer file
    writer.close()
    print("** Data Saved!!")


def read_catalog():
 try:
    global data_file
    global last_id
    reader = open(data_file, "rb")# reads file
    temp_list = pickle.load(reader)

    for item in temp_list:
        catalog.append(item)

    last = catalog[-1]
    last_id = last.id


    how_many = len(catalog)
    print("*** Loaded " + str(how_many) + " items")
 except:
    print("** No data file found, db is empty")


def save_log():
    global log_file
    writer = open(log_file, "wb")# create file (overwirte if file exists), and open it to Write Binary
    pickle.dump(log, writer) # dump catalog data into the writer file
    writer.close()
    print("** Log Saved!!")

def read_log():
 try:
    global log_file
    global last_id
    reader = open(log_file, "rb")# reads file
    temp_list = pickle.load(reader)

    for item in temp_list:
        log.append(item)

    last = log[-1]
    last_id = last.id


    how_many = len(log)
    print("*** Loaded " + str(how_many) + " log entries")
 except:
    print("** Error loading log entries")



# functions
def register_item():
    global last_id
    header("Register new Item")
    #print("-" * 30)
    title = input("New item title: ")
    cat = input("New item category: ")
    price = float(input("New item price: "))
    stock = int(input("New item stock: "))

    new_item = Item() # <-- this is how you create instance of a class (objects)
    last_id += 1 # No last_id++ :()
    new_item.id = last_id
    new_item.title = title
    new_item.category = cat
    new_item.price = price
    new_item.stock = stock 

    catalog.append(new_item)
    add_log_event("NewItem", "Added: " + str(last_id))
    print("Item created! ")

   
    print("Item created!")



def display_catalog():
  size = len(catalog)
  header("Current Catalog (" + str(size) + " items)")
  
  #print("-" * 70)
  print("|" + 'ID'.rjust(2) + " | " + 'Title'.ljust(20) + "|" + 'Category'.ljust(15) + "|" + 'Price'.rjust(10) + "|" + 'Stock'.rjust(5) + "|")
  print("-" * 70)

  for item in catalog:
      print("|" + str(item.id).rjust(2) + " | " + item.title.ljust(20) + "|" + item.category.ljust(15) + "|" + str(item.price).rjust(10) + "|" + str(item.stock).rjust(5) + "|") 

  
  
def display_not_stock():
    size = len(catalog)
    header("Out of Stock (" + str(size) + "items)")
    for item in catalog:
            if(item.stock == 0):
                print("|" + str(item.id).rjust(2) + " | " + item.title.ljust(20) + "|" + item.category.ljust(15) + "|" + str(item.price).rjust(10) + "|" + str(item.stock).rjust(5) + "|") 





def update_stock():
    display_catalog()
    selected_id = int(input("Enter the id of the item you want to select "))

    for item in catalog:
      if(selected_id == item.id):

        item.stock = int(input("Enter the items new stock number "))
        save_catalog()
     
    if(selected_id != item.id):
        print("Please enter a valid id")


def register_sale():
    display_catalog()
    selected_id = int(input("Enter the id of the item you want to select "))
    
    for item in catalog:
      if(selected_id == item.id):
        sold = int(input("How much of the item are you buying "))

        item.stock -= sold
       
        save_catalog()
        break
     
    if(selected_id != item.id):
        print("Please enter a valid id")




def totalvalue():
    total = 0.0
    maxNumber = total
    for item in catalog:
        total += (item.price * item.stock)
        
    print("Total Stock Value: $" + str(total))








def remove_item():
    display_catalog()
    id = int(input("Select the id of the item to remove"))
    found = False
    for item in catalog:
        if(item.id == id):
            catalog.remove(item)
            found = True
            add_log_event("Removed", "Removed item : " + str(item.id) )
            break

    if(found):
        print("Item remove from catalog")
    else:
        print("**Error: selected id its incorrect, try again!")



def get_current_time():
    now = datetime.datetime.now()
    return now.strftime("%M/%D/%Y %T")





def add_log_event(event_type, event_description):
    entry = get_current_time() + " | " + event_type.ljust(10) + " | " + event_description
    log.append(entry)
    save_log()






def print_log():
    header("Log of events")
    for entry in log:
        print(entry)

    input("Press enter to continue")


def show_unique():
    for item in unique_categories:
        print("|" + str(item.id).rjust(2) + " | " + item.title.ljust(20) + "|" + item.category.ljust(15) + "|" + str(item.price).rjust(10) + "|" + str(item.stock).rjust(5) + "|")



def display_categories():
  display_catalog()
  user_input = input("Select the name of the item to display: ")

  for item in catalog:
    if(item.category == user_input ):
       unique_categories.append(item)
       show_unique()
       input("Press enter to continue")
             
           
            



# instructions





    

    
#start menu

#first load data
read_catalog()
read_log()
input("Press enter to continue")

opc = " "
while(opc != 'x'):
    clear()
    menu()
    print("\n")
    opc = input("Please select an option: ")

    if(opc == '1'):
        register_item()
        save_catalog()
    elif(opc == '2'):
        display_catalog()
        totalvalue()
        
    elif(opc == '3'):
        display_not_stock()
    
    elif(opc == '4'):
        update_stock()

    elif(opc == '5'):
        totalvalue()

    elif(opc == '6'):
        remove_item()
        save_catalog()
    
    elif(opc == '7'):
        register_sale()
        save_catalog()

    elif(opc == '8'):
         remove_item()
       

    elif(opc == '9'):
      display_categories()
     





input("press enter to continue...")



   
    