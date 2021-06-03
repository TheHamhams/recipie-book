class Recipe:
    def __init__(self, name, category):
        self.name = name
        self.ingredients = {}
        self.steps = []
        self.tags = []
        self.category = category
        

    def add_ingredient(self, ingredient, amount):
        self.ingredients[ingredient.lower()] = amount

    def add_step(self, step):
        self.steps.append(step)

    def print_recipe(self):
        print(f"\n{self.name}")
        print("\nIngredients:")
        self.print_ingredients()
        print("\nSteps:")
        self.print_steps()
        print("\nTags:") 
        self.print_tags()
        

    def print_ingredients(self):
        for key, value in self.ingredients.items():
            print(f"{value} - {key}")


    def print_steps(self):
        i = 0
        while i < len(self.steps):
            print(f"{i + 1} - {self.steps[i]}")
            i += 1

    def print_tags(self):
        print(self.tags)

    def edit_category(self, category):
        pass

    def add_tag(self, tag):
        self.tags.append(tag.lower())
        print(f"{tag} added")
        print(self.tags)

    def print_tags(self):
        print(self.tags)
