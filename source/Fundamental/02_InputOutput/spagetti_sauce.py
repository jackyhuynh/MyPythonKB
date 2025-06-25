"""
LAB 2

This is the original text
# A spaghetti sauce recipe calls for the following ingredients:
# 2 cups of tomato sauce
# 1/3 cup of tomato paste (.333)
# 2 cloves garlic
# The recipe produces 4 servings with this amount of ingredients.  Write a program that asks the user how many servings they want to make, then displays the amount of each ingredient needed for the specified number of servings.
# 1 tablespoon oregano

"""

"""

PSEUDOCODE

Define function Spaghetti Sauce Caculator(number_of_serving -> #):
    tomato_sauce is equal to # * 2
    cup_of_tomato_paste is equal to # / 3
    glove_of_garlic is equal to # * 2
    tablespoon_oregano is equal to #
    return tomato_sauce, cup_of_tomato_paste, glove_of_garlic, tablespoon_oregano

main function:
    Get UserInput (number_of_serving)
    ST Happen to process that input
    Display/Output:

"""


# Define function Spaghetti Sauce Caculator(number_of_serving -> #):
#     tomato_sauce is equal to # / 2
#     cup_of_tomato_paste is equal to # / 12
#     glove_of_garlic is equal to # / 2
#     tablespoon_oregano is equal to # /4
#     return tomato_sauce, cup_of_tomato_paste, glove_of_garlic, tablespoon_oregano


def calculate_spaghetti_sauce(number_of_serving):
    tomato_sauce = number_of_serving / 2
    cup_of_tomato_paste = number_of_serving / 12
    glove_of_garlic = number_of_serving / 2
    tablespoon_oregano = number_of_serving / 4
    return tomato_sauce, cup_of_tomato_paste, glove_of_garlic, tablespoon_oregano


if __name__ == "__main__":
    number_of_serving = float(input("Enter the number of serving spaghetti sauce you want to make: "))

    # Calculate the total and average cost
    total_tomato_sauce, total_cup_of_tomato_paste, total_glove_of_garlic, total_tablespoon_oregano = calculate_spaghetti_sauce(
        number_of_serving)
    print(f"To make {number_of_serving} of spaghetti sauce you will need:")
    print(f"{total_tomato_sauce} cup of tomato sauce")
    print(f"{total_tablespoon_oregano} tablespoon of oregano")
    print(f"{total_glove_of_garlic} glove of garlic")
    print(f"{total_cup_of_tomato_paste} cup of tomato paste")
