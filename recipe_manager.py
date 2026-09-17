import json

class Recipe:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

    def __str__(self):
        return f"Recipe: {self.name}\nIngredients: {', '.join(self.ingredients)}\nInstructions: {self.instructions}"

    def to_dict(self):
        return {
            'name': self.name,
            'ingredients': self.ingredients,
            'instructions': self.instructions
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['ingredients'], data['instructions'])

class RecipeManager:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def remove_recipe(self, recipe_name):
        self.recipes = [recipe for recipe in self.recipes if recipe.name != recipe_name]

    def get_recipe(self, recipe_name):
        for recipe in self.recipes:
            if recipe.name == recipe_name:
                return recipe
        return None

    def list_recipes(self):
        return [recipe.name for recipe in self.recipes]

    def search_recipes(self, keyword):
        return [recipe for recipe in self.recipes
                if keyword.lower() in recipe.name.lower() or
                   any(keyword.lower() in ingredient.lower() for ingredient in recipe.ingredients)]

    def edit_recipe(self, recipe_name, new_name=None, new_ingredients=None, new_instructions=None):
        recipe = self.get_recipe(recipe_name)
        if recipe:
            if new_name:
                recipe.name = new_name
            if new_ingredients:
                recipe.ingredients = new_ingredients
            if new_instructions:
                recipe.instructions = new_instructions
        else:
            print(f"Recipe '{recipe_name}' not found.")

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump([recipe.to_dict() for recipe in self.recipes], file)

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.recipes = [Recipe.from_dict(recipe_data) for recipe_data in data]
        except FileNotFoundError:
            print(f"File '{filename}' not found. Starting with an empty recipe list.")