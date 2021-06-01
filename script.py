from hash import HashMap
from recipe import Recipe

categories = []
bad_input = "\nI'm sorry, I didn't recognize that command. Please try again.\n"
test = HashMap('test', 25)
testipe = Recipe("Testipe", test)
pizzape = Recipe("Pizzape", test)
test.assign("testipe", testipe)
testipe.add_ingredient("cheese", "2 cups")
testipe.add_ingredient("Crackers", "4")
testipe.add_step("Melt the cheese")
testipe.add_step("Dip the crackers in the cheese")
testipe.add_tag("cheesy")
testipe.add_tag("Cholesterol")
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
    recipe_name = input("\nWhat is the name of your recipe?\n").lower()
    confirm = input(f"You entered '{recipe_name}', is this correct? (yes/no) ").lower()
    if confirm != 'yes':
        add_recipe_menu(category)
    # create recipie object and add it to the category hash map
    recipe = Recipe(recipe_name, category)
    category.assign(recipe_name, recipe)
    print(f"You added '{recipe.name}' to '{category.name}'")
    add_ingredient_menu(recipe)
    
def add_ingredient_menu(recipe):
    recipe.print_ingredients()
    ingredient = input("What is the name of the ingredient you would like to add?\n")
    ammount = input("How much?")
    recipe.add_ingredient(ingredient, ammount)
    response = input("Would you like to add another ingredient? (yes/no) ").lower()
    if response == 'yes':
        add_ingredient_menu(recipe)
    else: 
        if recipe.steps == []:
            add_step_menu(recipe)
        else: 
            category_menu(recipe.category)

    
def add_step_menu(recipe):
    recipe.print_steps()
    step = input("What is the next step?\n")
    recipe.add_step(step)
    response = input("Would you like to add another step? (yes/no) ").lower()
    if response == 'yes':
        add_step_menu(recipe)
    else: 
        if recipe.tags == []:
            add_tag_menu(recipe)
        else: 
            category_menu(recipe.category)

def add_tag_menu(recipe):
    recipe.print_tags()
    step = input("What is the next step?\n")
    recipe.add_tag(step)
    response = input("Would you like to add another tag? (yes/no) ").lower()
    if response == 'yes':
        add_tag_menu(recipe)
    else: 
        category_menu(recipe.category)

def delete_recipe_menu(category):
    pass

def select_recipe(category):
    recipe_list = []
    for recipe in category.array:
        if recipe != None:
            recipe_list.append(recipe[1].name)
    print(recipe_list)
    response = input("Which recipe would you like to select?\n").lower()
    recipe = category.retrieve(response) 
    if recipe != None:
        recipe.print_recipe()
    else:
        print(f"I am sorry, I could not find {response}, please try again.")
        select_recipe(category)
        
    


def exit_book():
    print("\nHappy cooking!")
    exit()


#program_start()
select_recipe(test)
