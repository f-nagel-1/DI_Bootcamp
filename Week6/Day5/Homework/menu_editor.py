# Create a file called menu_editor.py , which will have the following functions:
# load_manager()- this function should create a new MenuItem instance.

# show_user_menu() - this function should display the program menu (not the restaurant menu!), and ask the user to choose an item. Call the appropriate function that matches the user’s input.

from xp import MenuItem

def load_manager():
    return MenuItem

def show_user_menu():
    print("(a) Add a new item\n (d) Delete an item\n (v) View the menu\n (x) Exit")

def add_item_to_menu(item_name, item_price):
    return load_manager().save(item_name, item_price)

def remove_item_from_menu():
    return load_manager().delete(item_name)

def show_restaurant_menu():
    return load_manager().all()
    

def main():
    while True:
        show_user_menu()
        while True:
            option = input('\nPlease select a menu option to continue. a,d,v,or x: ')
            if option in ('a','d','v','x'):
                break
            else:
                print('Please enter valid menu option')
        if option == "a":
            item_name = input("Please enter an item name\n")
            item_price = input("Please enter an item price\n")
            print(add_item_to_menu(item_name, item_price))

        if option == "d":
            item_name = input("Please enter an item name\n")
            print(remove_item_from_menu(item_name))

        if option == "v":
            menu = show_restaurant_menu()
            print(menu)

        if option == "x":
            menu = show_restaurant_menu()
            print(menu)
            break
            

    

main()


# remove_item_from_menu()- this function should ask the user to input the name of the item they want to remove from the restaurant’s menu. The function should not interact with the menu itself, but simply call the appropriate function from the MenuItem object.
# If the item was deleted successfully – print a message to let the user know this was completed.
# If not – print a message which states that there was an error.