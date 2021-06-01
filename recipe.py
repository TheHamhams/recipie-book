class Recipe:
    def __init__(self, name, category):
        self.name = name
        self.ingredients = {}
        self.steps = []
        self.tags = []
        self.category = category
        

    def add_ingredient(self, ingredient, ammount):
        self.ingredients[ingredient] = ammount

    def edit_ingredients(self):
        pass

    def add_step(self, step):
        self.steps.append(step)

    def print_recipe(self):
        pass

    def print_ingredients(self):
        for key, value in self.ingredients.items():
            print(f"{value}: {key}")


    def print_steps(self):
        i = 0
        while i < len(self.steps):
            print(f"{i + 1} - {self.steps[i]}")
            i += 1

    def print_tags(self):
        pass

    def edit_category(self, category):
        pass

    def print_category(self):
        pass

    def add_tag(self, tag):
        self.tags.append(tag)

    def edit_tag(self):
        pass

    def print_tags(self):
        print(self.tags)
