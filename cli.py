from recipe_manager import Recipe, RecipeManager

def main():
    manager = RecipeManager()
    manager.load_from_file('data/recipes.json')  # Load existing recipes from file on startup

    while True:
        # Main menu - loops until user chooses to exit
        print("\nRecipe Manager")
        print("1. Add Recipe")
        print("2. View Recipes")
        print("3. Search Recipes")
        print("4. Edit Recipe")
        print("5. Delete Recipe")
        print("6. Save Recipes")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            # Add a new recipe - collect details and create a Recipe object
            name = input("Enter recipe Title: ")
            ingredients = input("Enter ingredients (comma-separated): ").split(',')  # turn into a list
            instructions = input("Enter instructions: ")
            recipe = Recipe(name, ingredients, instructions)
            manager.add_recipe(recipe)

        elif choice == '2':
            # View all recipes - currently just shows names (list_recipes only returns names)
            recipes = manager.list_recipes()
            if recipes:
                print("Recipes:")
                for recipe_name in recipes:
                    print(f"- {recipe_name}")
            else:
                print("No recipes found.")

        elif choice == '3':
            # Search recipes by keyword (checks title and ingredients)
            keyword = input("Enter keyword to search: ")
            results = manager.search_recipes(keyword)
            if results:
                print("Search Results:")
                for recipe in results:
                    print(f"- {recipe.name}")
            else:
                print("No matching recipes found.")

        elif choice == '4':
            # Edit an existing recipe - blank input means "don't change this field"
            name = input("Enter the name of the recipe to edit: ")
            new_name = input("Enter new name (leave blank to keep current): ")
            new_ingredients = input("Enter new ingredients (comma-separated, leave blank to keep current): ")
            new_instructions = input("Enter new instructions (leave blank to keep current): ")

            manager.edit_recipe(
                name,
                new_name if new_name else None,
                new_ingredients.split(',') if new_ingredients else None,
                new_instructions if new_instructions else None
            )

        elif choice == '5':
            # Delete a recipe by name
            name = input("Enter the name of the recipe to delete: ")
            manager.remove_recipe(name)

        elif choice == '6':
            # Manually save current recipes to file
            manager.save_to_file('data/recipes.json')
            print("Recipes saved.")

        elif choice == '7':
            # Save and exit
            manager.save_to_file('data/recipes.json')
            print("Exiting. Recipes saved.")
            break

if __name__ == "__main__":
    main()