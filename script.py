from hash import HashMap
from recipe import Recipe

categories = []
bad_input = "\nI'm sorry, I didn't recognize that command. Please try again.\n"
test = HashMap('test', 25)
testipe = Recipe("Testipe")
pizzape = Recipe("Pizzape")
test.assign("testipe", testipe)
test.assign("pizzape", pizzape)
categories.append(test)

def program_start():
    print("Welcome to your recipe book! What would you like to do?")
    response = input("""
    Choose from the following options:

    'category': Choose a category to open
    'add': Add a new category
    'delete': delete an existing category
    'ingredient': Search for recipes that contain a certain ingredient
    'tag': Search for recipes that contain a certain tag
    'exit': Exit program

    """).lower()
    if response == 'category':
        category_select()
    elif response == 'add':
        add_category_menu()
    elif response == 'delete':
        delete_category_menu()
    elif response == 'ingredient':
        ingredient_search_menu()
    elif response == 'tag':
        tag_search_menu()
    elif response == 'exit':
        exit_book()
    else:
        print(bad_input)
        program_start()


def category_select():
    print_categories()
    response = input("\nWhat category would you like to select?\n").lower()
    choice = None
    for category in categories:
        if response == category.name:
            choice = category
    if choice == None:
        print(bad_input)
        category_select()
    else: 
        category_menu(choice)

def print_categories():
    lst = []
    for category in categories:
        lst.append(category.name)
    print(lst)


def category_menu(category):
    response = input(f"""
    {category.name}

    'add': Add a new recipe
    'delete': Delete a recipe
    'select': Select a recipe by name
    'main': Go back to main menu
    'exit': Exit program

    """).lower()

    if response == 'add':
        add_recipe_menu(category)
    elif response == 'delete':
        delete_recipe_menu(category)
    elif response == 'select':
        select_recipe(category)
    elif response == 'main':
        program_start()
    elif response == 'exit':
        exit_book()
    else:
        print(bad_input)
        category_menu(category)

def add_category_menu():
    pass

def delete_category_menu():
    pass


def ingredient_search_menu():
    pass

def tag_search_menu():
    pass

def add_recipe_menu(category):
    pass

def delete_recipe_menu(category):
    pass

def select_recipe(category):
    pass

def exit_book():
    print("\nHappy cooking!")
    exit()


program_start()