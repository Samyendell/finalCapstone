from tabulate import tabulate

#========The beginning of the class==========
# Class for Shoe
class Shoe:

# Initalise Shoe with the following attributes
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

# Method to return the cost
    def get_cost(self):
        return f"The cost of the product is {self.cost}"

# Method to return the quantity
    def get_quantity(self):
        return f"The quantity of the order is {self.quantity}"

# Methods to print the instance of an object      
    def __str__(self):
        return f"Country of order : {self.country}\nOrder code : {self.code}\nProduct : {self.product}\nCost : {self.cost}\nQuantity : {self.quantity}"

    def __repr__(self) -> str:
        return str(self)
#=============Shoe list===========

shoe_list = []

#==========Functions outside the class==============

def read_shoes_data():
    '''Function to read the data from "inventory.txt", 
    format it as a instance "Shoe" and store it in "shoe_list"
    '''
    # store the data in the file, if the files empty display message
    try:
        with open("inventory.txt", "r") as inventory_doc:
            inventory_file = inventory_doc.readlines()
            

    except:
        print("There isn't any orders yet")
    
    # Create a instance of "Shoe" for each line of data
    for count,line in enumerate(inventory_file):
        if count > 0:
            
            
            line = line.split(",")
            product = Shoe(line[0], line[1], line[2], line[3], line[4])
            shoe_list.append(product)
    

def capture_shoes():
    '''Function to allow the user to create a instance of "Shoe" and 
    store it in "shoe_list"
    '''
    
    # Store the needed data from the user to create a instance of "Shoe"
    while True:

        try:
            user_country = input("What is the country of the order : ")
            user_code = input("What is the product code of the order : ")
            user_product = input("What is the name of the product : ")
            user_cost = float(input("What is the cost of the order : "))
            user_quantity = int(input("What is the quantity of the order : "))
            break
        except:
            print("Invalid data entered, please try again (the cost and quantity must be numbers)")
            continue

    # Create a instance of "shoe" and add it to "shoe_list"
    user_order = Shoe(user_country, user_code, user_product, user_cost, user_quantity)
    shoe_list.append(user_order)
    print(shoe_list)


def view_all():
    '''Function to display all the items in "shoe_list"
    '''

    read_shoes_data()

    shoe_list_display = []
    start = 0
    end = 1
    # format the data in "shoe_list" into a two dimensional list so it can be tabulated
    for line in range(len(shoe_list)):
        
        shoe_list_display.append(shoe_list[start:end])
        start += 1
        end += 1 
   
    shoe_list_display_tab = tabulate(shoe_list_display)
    
    print(shoe_list_display_tab)
   

def re_stock():
    '''Function to find the instance of shoe with the lowest quantity
    and display it. Then allow the user to add to this value and overwrite
    this in the orginal file "inventory.txt" 
    '''
    quantity_list = []
    low_shoe_display = []
    # store the data in the file, if the files empty display message
    try:
        with open("inventory.txt", "r") as inventory_doc:
            inventory_file = inventory_doc.readlines()
    except:
        print("There isn't any products yet")
            
    # Create a new list and append all the quantity values
    for count,line in enumerate(inventory_file):
        if count > 0:
            line = line.split(",")
            quantity_list.append(line[4])
    
    quantity_list = ",".join(quantity_list)
    quantity_list = quantity_list.split("\n,")

    # change all the quantity values from strings to integers
    for i in range(len(quantity_list)):
        quantity_list[i] = int(quantity_list[i])
    
    # get the index of the smallest quantity value    
    min_index = quantity_list.index(min(quantity_list))
    
    # find the item with the smallest quantity and store it twice
    # once for displaying and once to add to
    for count,line in enumerate(inventory_file):
        if count == min_index + 1:
            stored_product = "".join(line)
            stored_product = stored_product.split(",")

            line = line.split(",")
            product = Shoe(line[0], line[1], line[2], line[3], line[4])
            low_shoe_display.append(product)

    # Format the data so it can be tabulated and display it
    low_shoe_display1 = []
    start = 0
    end = 1
 
    for line in range(len(low_shoe_display)):
        
        low_shoe_display1.append(low_shoe_display[start:end])
        start += 1
        end += 1

    low_shoe_display_tab = tabulate(low_shoe_display1) 
    print(low_shoe_display_tab)
            
    # Allow the user to add to the quantity value 
    for line in low_shoe_display:
        while True:
            add_stock = input("Would you to add stock to above item?")

            if add_stock.lower() == "yes":
                try:
                    print(line)
                    add_stock_amount = int(input("How much would you like to add ?"))
    
                    stored_product[4] = int(stored_product[4])
                    stored_product[4] += add_stock_amount
                    break

                except:
                    print("Invalid data entered, please try again (must be a whole number)")
                    continue
            elif add_stock.lower() == "no":
                break
            
            else:
                print("Invalid data entered, please try again (yes or no)")
                continue
            
    # Overwrite the data in the orginal file
    for count,line in enumerate(inventory_file):
        if count == min_index + 1:
            inventory_file[count] = stored_product


    with open("inventory.txt", "w") as inventory_file_write:
        for count,line in enumerate(inventory_file):
            if count == min_index + 1: 
                line[4] = str(line[4])
                line[4] = line[4] + "\n"
                line = ",".join(line)
            inventory_file_write.write(line)


def seach_shoe():
    '''Function to find the item with the provided product code and display it 
    '''
    search_display = []
    search_display_tab = []

    # store the data in the file, if the files empty display message
    try:
            with open("inventory.txt", "r") as inventory_doc:
                inventory_file = inventory_doc.readlines()

    except:
        print("There isn't any products yet")

    # Find the item with the entered product code and stored it
    while True:
        code_search = input("Enter the product code for the shoe you would to view : (enter quit to exit)")

        for line in inventory_file:
            if code_search in line:
                
                print(line)
                line = "".join(line)
                line = line.split(",")
                search_display.append(line)

        if code_search.lower() == "quit":
            break
        
        elif len(search_display) == 0:
            print("No product found, please try again")
            continue

        # display the searched for item
        else:
            
            search_display_tab = tabulate(search_display)
            
            print(search_display_tab)
            break   

def value_per_item():
    '''Function to calculate the value of each item in "inventory.txt".
    Then display all the items with a value column 
    '''
    # store the data in the file, if the files empty display message
    try:
        with open("inventory.txt", "r") as inventory_doc:
            inventory_file = inventory_doc.readlines()

    except:
        print("There isn't any products yet")

    value_list_display = []
    value_list_display_tab = []
    
    # Calculate the value for each item and add it to the list for each item
    for count,line in enumerate(inventory_file):
        if count == 0:
            line = "".join(line)
            line = line.split(",")
            line.append("Value")
            value_list_display.append(line)

        else:
            line = "".join(line)
            line = line.split(",")

            line[3] = int(line[3])
            line[4] = int(line[4]) 
            value = line[3] * line[4]
            line.append(value)
            value_list_display.append(line)
    
    # diplays all the items with value 
    value_list_display_tab = tabulate(value_list_display,headers = "firstrow" )
    
    print(value_list_display_tab)
    

def highest_qty():
    '''Function to find the item with the highest quantity and diplay it with a message
    '''

    quantity_list = []
    high_shoe_display = []
    # store the data in the file, if the files empty display message
    try:
        with open("inventory.txt", "r") as inventory_doc:
            inventory_file = inventory_doc.readlines()
    except:
        print("There isn't any products yet")
            
    # Create a new list and append all the quantity values
    for count,line in enumerate(inventory_file):
        if count > 0:
            line = line.split(",")
            quantity_list.append(line[4])

    quantity_list = ",".join(quantity_list)
    quantity_list = quantity_list.split("\n,")

    # change all the quantity values from strings to integers
    for i in range(len(quantity_list)):
        quantity_list[i] = int(quantity_list[i])

    # get the index of the smallest quantity value 
    min_index = quantity_list.index(max(quantity_list))
    
    # find the item with the smallest quantity and store it twice
    # once for displaying and once to add to
    for count,line in enumerate(inventory_file):
        if count == min_index + 1:
            stored_product = "".join(line)
            stored_product = stored_product.split(",")
            
            line = line.split(",")
            
            product = Shoe(line[0], line[1], line[2], line[3], line[4])
            high_shoe_display.append(product)

    # Format the data so it can be tabulated and display it with a message
    high_shoe_display1 = []
    start = 0
    end = 1

    for line in range(len(high_shoe_display)):
        
        high_shoe_display1.append(high_shoe_display[start:end])
        start += 1
        end += 1

    low_shoe_display_tab = tabulate(high_shoe_display1) 
    print(low_shoe_display_tab)

    print("This shoe is for sale!")
    

#==========Main Menu=============
# Main menu to allow the user to run the above functions and exit when they would like
while True:
    try:
        user_option = int(input('''Enter a option from the menu below:
    1 = Load product data from text file into product list
    2 = Add a product to the product list    
    3 = View all the products in the product list
    4 = Find the product with the lowest stock and give the option to add stock
    5 = Search for a product using the product code
    6 = Display all products with the total value of stock
    7 = Display the product with the highest stock 
    8 = Exit the menu
    :'''))

    except:
        print("Invalid data entered, please try again (a whole number must be entered)")
    
    if user_option == 1:
        read_shoes_data()
        continue
    elif user_option == 2:
        capture_shoes()
        print("2")
    elif user_option == 3:
        view_all()
        continue
    elif user_option == 4:
        re_stock()
        continue
    elif user_option == 5:
        seach_shoe()
        continue
    elif user_option == 6:
        value_per_item()
        continue
    elif user_option == 7:
        highest_qty()
        continue
    elif user_option == 8:
        break

    else:
        print("Invalid data entered, please try again")
        continue