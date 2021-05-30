class Recipe:
    def __init__(self, name):
        self.name = name
        self.ingredients = []
        self.steps = []
        self.tags = []
        

    def add_ingredients(self, ingredient):
        pass

    def edit_ingredients(self):
        pass

    def add_steps(self):
        pass

    def print_recipe(self):
        pass

    def print_ingredients(self):
        pass

    def print_steps(self):
        pass

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
