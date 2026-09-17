import json  # for saving/loading recipes as JSON


class Recipe:
    """Represents a single recipe with a name, ingredients, and instructions."""

    def __init__(self, name, ingredients, instructions):
        self.name = name                    # recipe title
        self.ingredients = ingredients      # list of ingredient strings
        self.instructions = instructions    # instructions as a single string

    def __str__(self):
        # Controls how a Recipe looks when printed - joins ingredients into
        # a readable comma-separated list instead of showing the raw list
        return f"Recipe: {self.name}\nIngredients: {', '.join(self.ingredients)}\nInstructions: {self.instructions}"

    def to_dict(self):
        # Converts this Recipe object into a plain dictionary,
        # since JSON can only store basic types (dict/list/str/etc), not objects
        return {
            'name': self.name,
            'ingredients': self.ingredients,
            'instructions': self.instructions
        }

    @classmethod
    def from_dict(cls, data):
        # Rebuilds a Recipe object from a plain dictionary (the reverse of to_dict)
        # Used when loading recipes back in from the JSON file
        # cls refers to the class itself (Recipe), so this returns a new Recipe instance
        return cls(data['name'], data['ingredients'], data['instructions'])


class RecipeManager:
    #Manages a collection of Recipe objects - add, view, search, edit, delete, save/load.

    def __init__(self):
        self.recipes = []  # holds all Recipe objects in memory

    def add_recipe(self, recipe):
        # Adds a new Recipe object to the collection
        self.recipes.append(recipe)

    def remove_recipe(self, recipe_name):
        # Rebuilds self.recipes, keeping every recipe EXCEPT the one matching recipe_name
        self.recipes = [recipe for recipe in self.recipes if recipe.name != recipe_name]

    def get_recipe(self, recipe_name):
        # Finds and returns the first recipe with a matching name (exact match)
        # Returns None if nothing matches
        for recipe in self.recipes:
            if recipe.name == recipe_name:
                return recipe
        return None

    def view_recipe(self, recipe_name):
        # Returns the string representation of a recipe, or a message if not found
        recipe = self.get_recipe(recipe_name)
        if recipe:
            return str(recipe)
        else:
            return f"Recipe '{recipe_name}' not found."

    def list_recipes(self):
        # Returns just the names of all recipes (quick summary list)
        return [recipe.name for recipe in self.recipes]

    def search_recipes(self, keyword):
        # Returns all recipes where the keyword appears in the title OR
        # in any of the ingredients - case-insensitive substring match
        return [recipe for recipe in self.recipes
                if keyword.lower() in recipe.name.lower() or
                   any(keyword.lower() in ingredient.lower() for ingredient in recipe.ingredients)]

    def edit_recipe(self, recipe_name, new_name=None, new_ingredients=None, new_instructions=None):
        # Finds the recipe by name, then updates only the fields that were
        # actually passed in (None = "don't change this field")
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
        # Writes all recipes to a JSON file
        # Each Recipe object is converted to a dict first, since json.dump
        # can't serialize custom objects directly
        with open(filename, 'w') as file:
            json.dump([recipe.to_dict() for recipe in self.recipes], file)

    def load_from_file(self, filename):
        # Reads recipes back in from a JSON file, rebuilding each as a Recipe object
        # If the file doesn't exist yet (e.g. first run), starts with an empty list
        # instead of crashing
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.recipes = [Recipe.from_dict(recipe_data) for recipe_data in data]
        except FileNotFoundError:
            print(f"File '{filename}' not found. Starting with an empty recipe list.")