"""
This program asks the user for a number in the range of 1-7 and
displays the corresponding day of the week.
If the user enters anything except the numbers 1-7,
an error message is displayed.
"""


# pylint: disable=no-else-return, too-many-return-statements
def get_day_if_elif_else(number):
    """
    Get the day of the week based on the number using if-elif-else logic.

    :param number: Number representing the day of the week (1-7)
    :return: Day of the week or an error message
    """
    if number == 1:
        return "Monday"
    elif number == 2:
        return "Tuesday"
    elif number == 3:
        return "Wednesday"
    elif number == 4:
        return "Thursday"
    elif number == 5:
        return "Friday"
    elif number == 6:
        return "Saturday"
    elif number == 7:
        return "Sunday"
    else:
        return "Error: Invalid number, please enter a number between 1 and 7."


def main_if_elif_else():
    """
    Main function to accept user input and display the corresponding day
    of the week using if-elif-else logic.
    """
    try:
        number = int(input("Enter a number (1-7): "))
        day = get_day_if_elif_else(number)
        print(day)
    except ValueError:
        print("Error: Please enter a valid integer.")


if __name__ == "__main__":
    main_if_elif_else()
