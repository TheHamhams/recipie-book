from hash import HashMap
from recipe import Recipe

# List that contains the category hash maps
categories = []

bad_input = "\nI'm sorry, I didn't recognize that command. Please try again.\n"

# Below are test variables to make testing easier
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

# Main menu for the program
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

# Menu to select existing category
def category_select():
    print_categories()
    response = input("\nWhat category would you like to select?\n").lower()
    choice = None
    # Checks to see if category exists
    for category in categories:
        if response == category.name:
            choice = category
    
    if choice == None:
        print(bad_input)
        category_select()
    else: 
        category_menu(choice)

# Method to print out the category names instead of the object
def print_categories():
    lst = []
    
    for category in categories:
        lst.append(category.name)
    print(lst)

# Menu for when a category is selected
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

# Creates new category hash map
def add_category_menu():
    response = input("What is the name of your new category?\n").lower()
    
    confirm = input(f"You entered '{response}', is this correct? (yes/no)\n").lower()
    
    if confirm == 'yes':
        new_category = HashMap(response, 25)
        categories.append(new_category)
        category_menu(new_category)
    else:
        add_category_menu()

# Menu to delete category and all recipies in it
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

# Adds recipe to currently selected category
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

# Adds ingredients to selected recipe    
def add_ingredient_menu(recipe):
    recipe.print_ingredients()
    
    ingredient = input("What is the name of the ingredient you would like to add?\n")
    
    amount = input("How much?")
    
    recipe.add_ingredient(ingredient, amount)
    
    response = input("Would you like to add another ingredient? (yes/no) ").lower()
    
    if response == 'yes':
        add_ingredient_menu(recipe)
    # Below brings you to the step menu if it is blank or back to the recipe menu if it is not
    else: 
        if recipe.steps == []:
            add_step_menu(recipe)
        else: 
            edit_recipe_menu(recipe)

# Adds step to selected recipe    
def add_step_menu(recipe):
    recipe.print_steps()
    
    step = input("What is the next step?\n")
    
    recipe.add_step(step)
    
    response = input("Would you like to add another step? (yes/no) ").lower()
    
    if response == 'yes':
        add_step_menu(recipe)
    # Brings you to tag menu if none are present in the recipe or back to recipe menu if not
    else: 
        if recipe.tags == []:
            add_tag_menu(recipe)
        else: 
            edit_recipe_menu(recipe)

# Adds tag to selected recipe
def add_tag_menu(recipe):
    recipe.print_tags()
    
    step = input("What tag would you like to add?\n")
    
    recipe.add_tag(step)
    
    response = input("Would you like to add another tag? (yes/no) ").lower()
    
    if response == 'yes':
        add_tag_menu(recipe)
    else: 
        edit_recipe_menu(recipe)

# Deletes recipe from selected category
def delete_recipe_menu(category):
    # Creates a readable list
    recipe_list = []
    for recipes in category.array:
        if recipes != None:
            recipe_list.append(recipes[1].name)
    # Kicks you back to category menu if no recipes exist in selected category
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

    
# Selects recipe from selected category
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
    
    # Checks if recipe exists
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


# Menu to select how selected recipe will be edited    
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
        edit_ingredients_menu(recipe)
    elif response == 'steps':
        edit_steps_menu(recipe)
    elif response == 'tags':
        edit_tags_menu(recipe)
    elif response == 'back':
        category_menu(recipe.category)
    elif response == 'main':
        program_start()
    elif response == 'exit':
        exit_book()
    else:
        print(bad_input)
        edit_recipe_menu(recipe)

# Menu to choose how ingredients are edited
def edit_ingredients_menu(recipe):
    recipe.print_ingredients()
    
    response = input("""
    What would you like to do?

    'add': Add new ingredients
    'edit': Change existing ingredient
    'delete': Delete an ingredient
    'back': Go back to recipe menu
    'main': Go main menu
    'exit': Exit program

    """).lower()

    if response == 'add':
        add_ingredient_menu(recipe)
    elif response == 'edit':
        edit_ingredients(recipe)
    elif response == 'delete':
        delete_ingredient(recipe)
    elif response == 'back':
        edit_recipe_menu(recipe)
    elif response == 'main':
        program_start()
    elif response == 'exit':
        exit_book()
    else:
        print(bad_input)
        edit_ingredients_menu(recipe)

# Method to replace existing ingredient with an updated one    
def edit_ingredients(recipe):
    if recipe.ingredients == {}:
        print("I am sorry, there are no ingredients in this recipe.")
        edit_recipe_menu(recipe)
    
    recipe.print_ingredients()
    
    response = input("Which ingredient would you like to change? (type in the ingredient's full name or 'none')\n").lower()
    
    if response == 'none':
        edit_recipe_menu(recipe)
    
    if response not in recipe.ingredients:
        print(f"I'm sorry, I couldn't find '{response}', please try again\n")
        edit_ingredients(recipe)
    
    new_ingredient = input("What is the new ingredient name? (ingredient name or 'same')\n").lower()
    
    # Changes ingredient ingredients and amounts or keeps them the same
    if new_ingredient == 'same':
        new_ingredient = response
    new_amount = input("What is the new amount? (new amount or 'same')\n").lower()
    
    if new_amount == 'same':
        new_amount = recipe.ingredients[response]
    
    # Replaces old ingredient and amount with new ones
    recipe.ingredients[new_ingredient] = recipe.ingredients.pop(response)
    recipe.ingredients[new_ingredient] = new_amount
    
    next = input("Would you like to edit another ingredient? (yes/no)\n").lower()
    
    if next == 'yes':
        edit_ingredients(recipe)
    else:
        edit_recipe_menu(recipe)

# Deletes ingredient from selected recipe
def delete_ingredient(recipe):
    if recipe.ingredients == {}:
        print("I am sorry, there are no ingredients in this recipe.")
        edit_recipe_menu(recipe)
    
    recipe.print_ingredients()
    
    response = input("Which ingredient would you like to delete? (ingredient name or 'none')\n").lower()
    
    if response == 'none':
        edit_recipe_menu(recipe)
    
    if response not in recipe.ingredients:
        print(f"I am sorry, I could not find '{response}', please try again.")
        delete_ingredient(recipe)
    else:
        confirm = input(f"Are you sure you would like to delete '{response}' (yes/no)\n").lower()
        
        if confirm == 'yes':
            del recipe.ingredients[response]
            next = input(f"'{response}' deleted, would you like to delete another ingredient? (yes/no)\n").lower()
            if next == 'yes':
                delete_ingredient(recipe)
            else:
                edit_recipe_menu(recipe)
        else:
            delete_ingredient(recipe)

# Menu to choose how steps are edited
def edit_steps_menu(recipe):
    recipe.print_steps()
    response = input("""
    What would you like to do?

    'add': Add new steps
    'edit': Change existing steps
    'delete': Delete a step
    'back': Go back to recipe menu
    'main': Go main menu
    'exit': Exit program

    """).lower()

    
    if response == 'add':
        add_step_menu(recipe)
    elif response == 'edit':
        edit_steps(recipe)
    elif response == 'delete':
        delete_step(recipe)
    elif response == 'back':
        edit_recipe_menu(recipe)
    elif response == 'main':
        program_start()
    elif response == 'exit':
        exit_book()
    else:
        print(bad_input)
        edit_steps_menu(recipe)

# Changes existing step
def edit_steps(recipe):
    if recipe.steps == []:
        print("I am sorry, there are no steps in this recipe.")
        edit_recipe_menu(recipe)
    
    recipe.print_steps()
    
    response = input("Which step would yo like to edit (enter step number or 'none')\n")
    
    if response == 'none':
        edit_recipe_menu(recipe)
    
    # Checks to make sure response is a valid step number
    if is_int(response) == False:
        edit_steps(recipe)
    
    # Adjusts response to match array index
    idx = int(response)
    idx -= 1
    
    if idx in range(len(recipe.steps)):
        new_step = input("What is the new step?\n")
        recipe.steps[idx] = new_step
        next = input("Would you like to edit another step? (yes/no)\n").lower()
        if next == 'yes':
            edit_steps(recipe)
        else:
            edit_recipe_menu(recipe)
    else:
        print(bad_input)
        edit_steps(recipe)

# Deletes existing step
def delete_step(recipe):
    if recipe.steps == []:
        print("I am sorry, there are no steps in this recipe.")
        edit_recipe_menu(recipe)
    
    recipe.print_steps()
    
    response = input("Which step would yo like to delete? (enter step number or 'none')\n")
    
    if response == 'none':
        edit_recipe_menu(recipe)
    
    if is_int(response) == False:
        edit_steps(recipe)
    
    # Adjusts response to match array index
    idx = int(response)
    idx -= 1
    
    if idx in range(len(recipe.steps)):
        confirm = input(f"Are you sure you would like to delete step '{response}'? (yes/no)\n").lower()
        
        if confirm == 'yes':
            recipe.steps.pop(idx)
        else:
            edit_recipe_menu(recipe)    
        next = input("Would you like to edit another step? (yes/no)\n").lower()
        if next == 'yes':
            edit_steps(recipe)
        else:
            edit_recipe_menu(recipe)
    else:
        print(bad_input)
        edit_steps(recipe)

# Checks if input is an int
def is_int(input):
    try:
        val = int(input)
        return True
    except ValueError:
        print("Sorry, that wasnt a number")
        return False

# Menu to choose how tags are edited
def edit_tags_menu(recipe):
    recipe.print_tags()
    
    response = input("""
    What would you like to do?

    'add': Add new tag
    'edit': Change existing tag
    'delete': Delete a tag
    'back': Go back to recipe menu
    'main': Go main menu
    'exit': Exit program

    """).lower()

    if response == 'add':
        add_tag_menu(recipe)
    elif response == 'edit':
        edit_tag(recipe)
    elif response == 'delete':
        delete_tag(recipe)
    elif response == 'back':
        edit_recipe_menu(recipe)
    elif response == 'main':
        program_start()
    elif response == 'exit':
        exit_book()
    else:
        print(bad_input)
        edit_steps_menu(recipe)

# Edit existing tag
def edit_tag(recipe):
    recipe.print_tags()
    
    response = input("Which tag would you like to edit? (enter tag name or 'none')\n").lower()

    if response == 'none':
        edit_recipe_menu(recipe)
    
    idx = 0

    if response in recipe.tags:
        idx = recipe.tags.index(response)
    else:
        print(f"I'm sorry, I couldn't find '{response}', please try again")
        edit_tag(recipe)

    new_tag = input("What would you like the new tag to be?\n").lower()

    recipe.tags[idx] = new_tag

    next = input("Would you like to edit another tag? (yes/no)\n").lower()

    if next == 'yes':
        edit_tag(recipe)
    else:
        edit_recipe_menu(recipe)

# Delete existing tag
def delete_tag(recipe):
    recipe.print_tags()
    
    response = input("Which tag would you like to delete? (enter tag name or 'none')\n").lower()

    if response == 'none':
        edit_recipe_menu(recipe)
    
    idx = 0

    if response in recipe.tags:
        idx = recipe.tags.index(response)
    else:
        print(f"I'm sorry, I couldn't find '{response}', please try again")
        edit_tag(recipe)

    confirm = input(f"Are you sure you would like to delete '{response}'? (yes/no)\n").lower()
    
    if confirm == 'yes':
        recipe.tags.pop(idx)
        
        next = input(f"'{response}' deleted, would you like to delete another tag? (yes/no)\n").lower()

        if next == 'yes':
            delete_tag(recipe)
        else:
            edit_recipe_menu(recipe)
    else:
        edit_recipe_menu(recipe)

# Exit command for program
def exit_book():
    print("\nHappy cooking!")
    exit()


#program_start()
edit_tags_menu(testipee)
