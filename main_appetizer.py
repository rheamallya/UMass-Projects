from appetizers import Appetizers_cat, read_csv


# read the CSV file into a list of Appetizers objects
appetizers = read_csv('appetizers.csv')


def write_recipe_to_file(recipe):
    with open("favorite_recipe.txt", "a") as f:
        f.write(f"{recipe.food_name}\n")
        f.write(f"Category: {recipe.category}\n")
        f.write(f"Recipe Type: {recipe.recipe_type}\n")
        f.write("Ingredients:\n")
        for ingredient in recipe.ingredients:
            f.write(f"- {ingredient}\n")
        f.write("\n")


while True:
    # ask the user to choose a category
    category = input("Please choose a category (Appetizer), or type 'exit' to quit: ")

    if category.lower() == 'exit':
        # exit the loop if the user types 'exit'
        break

    # filter the list of Appetizers objects to only those in the chosen category
    category_appetizers = [a for a in appetizers if a.category.lower() == category.lower()]

    if not category_appetizers:
        # if there are no appetizers in the chosen category, inform the user and continue to the next iteration of the loop
        print("Sorry, there are no appetizers in the chosen category.")
        continue

    # ask the user to choose a recipe type
    recipe_type = input("Please choose a recipe type (Chips and dip or Finger Foods): ")

   
    recipe_type_appetizers = [a for a in category_appetizers if a.recipe_type.lower() == recipe_type.lower()]

    if not recipe_type_appetizers:
        print("Sorry, there are no appetizers of the chosen recipe type.")
        continue

    food_name = input("Please choose a food name: ")


    chosen_appetizer = None
    for a in recipe_type_appetizers:
        if a.food_name.lower() == food_name.lower():
            chosen_appetizer = a
            break

    if chosen_appetizer is not None:
        print(f"The ingredients for {chosen_appetizer.food_name} are: {', '.join(chosen_appetizer.ingredients)}")
        print("You have chosen the following:")
        print(f"Category: {category}")
        print(f"Recipe Type: {recipe_type}")
        print(f"Food Name: {food_name}")
        
        # ask the user if they want to add the chosen recipe to the favorite recipes file
        choice = input("Do you want to add this recipe to your favorite recipes? (y/n): ")
        if choice.lower() == "y":
            write_recipe_to_file(chosen_appetizer)
            print("The recipe has been added to your favorite recipes.")
        else:
            print("The recipe has not been added to your favorite recipes.")
            
    else:
        print("Sorry, we couldn't find that food name in the chosen category and recipe type.")

    choice = input("Do you want to choose another recipe? (y/n): ")
    if choice.lower() == "n":
        break