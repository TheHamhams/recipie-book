from hash import HashMap
from recipe import Recipe

categories = []
bad_input = "\nI'm sorry, I didn't recognize that command. Please try again.\n"
test = HashMap('test', 25)
testipee = Recipe("testipee", test)
pizzape = Recipe("pizzape", test)
test.assign("testipee", testipee)
testipee.add_ingredient("cheese", "2 cups")
testipee.add_ingredient("Crackers", "4")
testipee.add_step("Melt the cheese")
testipee.add_step("Dip the crackers in the cheese")
testipee.add_tag("cheesy")
testipee.add_tag("Cholesterol")
test.assign("pizzape", pizzape)
categories.append(test)

def program_start():
    print("\nWelcome to your recipe book! What would you like to do?")
    response = input("""
    Choose from the following options:

    'category': Choose a category to open
    'add': Add a new category
    'delete': Delete an existing category
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
    response = input("What is the name of your new category?\n").lower()
    confirm = input(f"You entered '{response}', is this correct? (yes/no)\n").lower()
    if confirm == 'yes':
        new_category = HashMap(response, 25)
        categories.append(new_category)
        category_menu(new_category)
    else:
        add_category_menu()


def delete_category_menu():
    print_categories()
    response = input("Which category would you like to delete?\n").lower()
    for category in categories:
        if response == category.name:
            confirm = input(f"Are you sure you want to delete '{response}'? This will also delete all recipes in this category. (yes/no)\n")
            if confirm == 'yes':
                idx = categories.index(category)
                categories.pop(idx)
                program_start()
            else:
                program_start()
    print(f"'{response}', not found.")
    program_start()

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
            edit_recipe_menu(recipe)

    
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
            edit_recipe_menu(recipe)

def add_tag_menu(recipe):
    recipe.print_tags()
    step = input("What tag would you like to add?\n")
    recipe.add_tag(step)
    response = input("Would you like to add another tag? (yes/no) ").lower()
    if response == 'yes':
        add_tag_menu(recipe)
    else: 
        edit_recipe_menu(recipe)

def delete_recipe_menu(category):
    recipe_list = []
    for recipes in category.array:
        if recipes != None:
            recipe_list.append(recipes[1].name)
    if recipe_list == []:
        print(f"I am sorry, there seems to be no recipies yet in '{category.name}'\n")
        category_menu(category)
    print(recipe_list)
    response = input("Which recipe would you like to delete?? (recipe name / none)\n").lower()
    if response == 'none':
        category_menu(category)
    recipe = category.retrieve(response)
    if recipe == None:
        print(f"I am sorry, I could not find '{response}', please try again.")
        delete_recipe_menu(category)
    else:
        confirm = input(f"Are you sure you would like to delete '{response}'? (yes/no)\n")
        if confirm == 'yes':
            print(f"\n'{recipe.name}' deleted\n" )
            category.remove(recipe.name)
        else:
            delete_recipe_menu(category)
    next = input("Would you like to delete another recipe? (yes/no)\n")
    if next == 'yes':
        delete_recipe_menu(category)
    else:
        category_menu(category)

    

def select_recipe(category):
    recipe_list = []
    for recipes in category.array:
        if recipes != None:
            recipe_list.append(recipes[1].name)
    if recipe_list == []:
        empty = input(f"I am sorry, there seems to be no recipies yet in {category.name}, would you like to create one? (yes/no)\n").lower()
        if empty == 'yes':
            add_recipe_menu(category)
        else:
            category_menu(category)
    print(recipe_list)
    response = input("Which recipe would you like to select?\n").lower()
    recipe = category.retrieve(response) 
    if recipe != None:
        recipe.print_recipe()
    else:
        print(f"I am sorry, I could not find {response}, please try again.")
        select_recipe(category)
    next = input(f"""
    What would you like to do next?
    
    'edit': Edit recipe
    'delete': Delete recipe
    'next': Choose another recipe in '{category.name}'
    'main': Go back to main menu
    'exit': Exit program

    """).lower()
    if next == 'edit':
        edit_recipe_menu(recipe)
    elif next == 'delete':
        confirm = input(f"Are you sure you would like to delete '{recipe.name}'? (yes/no)\n")
        if confirm == 'yes':
            print(f"\n'{recipe.name}' deleted\n" )
            category.remove(recipe.name)
        select_recipe(category)   
    elif next == 'main':
        program_start()
    elif next == 'exit':
        exit_book()
    else:
        category_menu(category)


    
def edit_recipe_menu(recipe):
    recipe.print_recipe()
    response = input("""
    What would you like to edit?
    
    ingredients: Edit ingredients
    steps: Edit steps
    tags: Edit tags
    back: Go back to category menu
    main: Go back to main menu
    exit: Exit program

    """).lower()

    if response == 'ingredients':
        edit_ingredients(recipe)
    elif response == 'steps':
        edit_steps(recipe)
    elif response == 'tags':
        edit_tags(recipe)
    elif response == 'back':
        category_menu(recipe.category)
    elif response == 'main':
        program_start()
    elif response == 'exit':
        exit_book()
    else:
        print(bad_input)
        edit_recipe_menu(recipe)

def edit_ingredients(recipe):
    pass

def edit_steps(recipe):
    pass

def edit_tags(recipe):
    pass

def exit_book():
    print("\nHappy cooking!")
    exit()


program_start()

