class Recipe:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

    def __str__(self):
        return f"Recipe: {self.name}\nIngredients: {', '.join(self.ingredients)}\nInstructions: {self.instructions}"

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