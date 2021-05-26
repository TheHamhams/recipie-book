catagories = ['test']
bad_input = "\nI'm sorry, I didn't recognize that command. Please try again.\n"

def program_start():
    print("Welcome to your recipie book! What would you like to do?")
    response = input("""
    Choose from the following options:

    'catagory': Choose a catagory to open
    'add': Add a new catagory
    'delete': delete an existing catagory
    'ingredient': Search for recipies that contain a certain ingredient
    'tag': Search for recipies that contain a certain tag
    'exit': Exit program

    """).lower()
    if response == 'catagory':
        catagory_select()
    elif response == 'add':
        add_catagory_menu()
    elif response == 'delete':
        delete_catagory_menu()
    elif response == 'ingredient':
        ingredient_search_menu()
    elif response == 'tag':
        tag_search_menu()
    elif response == 'exit':
        exit_book()
    else:
        print(bad_input)
        program_start()


def catagory_select():
    # temporary commands till hash_map is created
    print(catagories)
    response = input("\nWhat catagory would you like to select?\n").lower()
    choice = None
    for catagory in catagories:
        if response == catagory:
            choice = catagory
    if choice == None:
        print(bad_input)
        catagory_select()
    else: 
        catagory_menu(choice)

def print_catagories():
    pass

def catagory_menu(catagory):
    print(f"You selected {catagory}")

def add_catagory_menu():
    pass

def delete_catagory_menu():
    pass


def ingredient_search_menu():
    pass

def tag_search_menu():
    pass

def exit_book():
    print("Happy cooking!")
    exit()


program_start()