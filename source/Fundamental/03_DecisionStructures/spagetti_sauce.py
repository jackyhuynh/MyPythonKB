# A spaghetti sauce recipe calculator based on per-serving ratios.

# --- CONSTANTS (Ratios per ONE serving) ---
# The user has specified the exact amount of each ingredient required for
# a single serving.
TOMATO_SAUCE_CUPS_PER_SERVING = 0.5
TOMATO_PASTE_CUPS_PER_SERVING = 1 / 12
GARLIC_CLOVES_PER_SERVING = 0.5
OREGANO_TBSP_PER_SERVING = 0.25


def calculate_ingredients(servings_to_make: float) -> tuple[float, float, float, float]:
    """
    Calculates the required amount of ingredients for a given number of servings.

    The calculation is a direct multiplication of the desired servings by the
    pre-defined per-serving ratio for each ingredient.

    Args:
        servings_to_make: The desired number of servings.

    Returns:
        A tuple containing the required amounts of:
        (tomato_sauce, tomato_paste, garlic, oregano)
    """
    if servings_to_make <= 0:
        return 0, 0, 0, 0

    needed_tomato_sauce = servings_to_make * TOMATO_SAUCE_CUPS_PER_SERVING
    needed_tomato_paste = servings_to_make * TOMATO_PASTE_CUPS_PER_SERVING
    needed_garlic_cloves = servings_to_make * GARLIC_CLOVES_PER_SERVING
    needed_oregano_tbsp = servings_to_make * OREGANO_TBSP_PER_SERVING

    return needed_tomato_sauce, needed_tomato_paste, needed_garlic_cloves, needed_oregano_tbsp


if __name__ == "__main__":
    try:
        # Get user input
        desired_servings = float(input("Enter the number of servings you want to make: "))

        if desired_servings <= 0:
            print("Please enter a positive number of servings.")
        else:
            # Calculate the required ingredients
            (
                total_tomato_sauce,
                total_tomato_paste,
                total_garlic_cloves,
                total_oregano_tbsp,
            ) = calculate_ingredients(desired_servings)

            # Display the results with formatted output
            print(f"\nTo make {desired_servings:g} servings, you will need:")
            print(f"- {total_tomato_sauce:.2f} cups of tomato sauce")
            print(f"- {total_tomato_paste:.2f} cups of tomato paste")
            print(f"- {total_garlic_cloves:.2f} cloves of garlic")
            print(f"- {total_oregano_tbsp:.2f} tablespoons of oregano")

    except ValueError:
        print("Invalid input. Please enter a valid number.")
