"""
This program asks the user for a number in the range of 1-7
and displays the corresponding day of the week.
If the user enters anything except the numbers 1-7,
an error message is displayed.
"""


# pylint: disable=line-too-long, no-else-return, too-many-return-statements, too-many-nested-blocks


def get_day_if_else_if(number):
    """
    Get the day of the week based on the number using if-else-if logic.

    :param number: Number representing the day of the week (1-7)
    :return: Day of the week or an error message
    """
    if number == 1:
        return "Monday"
    else:
        if number == 2:
            return "Tuesday"
        else:
            if number == 3:
                return "Wednesday"
            else:
                if number == 4:
                    return "Thursday"
                else:
                    if number == 5:
                        return "Friday"
                    else:
                        if number == 6:
                            return "Saturday"
                        else:
                            if number == 7:
                                return "Sunday"
                            else:
                                return "Error: Invalid number, please enter a number between 1 and 7."


def main_if_else_if():
    """
    Main function to accept user input and display the corresponding day of the week using if-else-if logic.
    """
    try:
        number = int(input("Enter a number from 1 to 7: "))
        day = get_day_if_else_if(number)
        print(day)
    except ValueError:
        print("Error: Please enter a valid integer.")


if __name__ == "__main__":
    main_if_else_if()
