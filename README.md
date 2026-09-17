# python_recipe_manager
Recipe Manager

A command-line app for managing recipes — built as part of my Python coursework. Lets you add, view, search, edit and delete recipes, and everything gets saved to a JSON file so it's still there next time you run it.

What it does
-Add a recipe with a title, ingredients and instructions
-Look up a single recipe by name and view in its entirety
-Search by keyword — checks both the title and the ingredients
-Edit a recipe (just leave a field blank if you don't want to change it)
-Delete a recipe (asks you to confirm first)
-Recipes save automatically when you exit, or manually from the menu

Files:
-recipe_manager.py   -> Recipe and RecipeManager classes, all the actual logic
-cli.py                -> the menu you actually interact with
-data/recipes.json     -> where your recipes get saved

Kept the classes and the CLI in separate files on purpose — logic in one place, user interaction in another.

Running it:

python cli.py

Then just follow the menu.

A few things worth knowing:
-Ingredients go in comma-separated, e.g. flour, sugar, eggs
-When editing, blank = "leave this as it is"
-First run with no save file yet? It just starts empty, no crash

Notes to self

Built this on top of the library inventory activity — same OOP shape (a "thing" class + a "manager" class), just applied to recipes instead of books. Main things that tripped me up: getting the if/elif ordering right for combo logic earlier in the course and a couple of silly bugs (splitting instructions into a list when they should've stayed a single string, and a misplaced else in the edit method that fired "not found" even when the recipe existed).