import random

# List of the 30 basic Python exercises
# These descriptions are taken directly from the 'python_exercises' document.
EXERCISES = [
    "1. Greeting Message: Write a program that asks the user for their name and then prints a personalized greeting message.",
    "2. Age Calculator: Ask the user for their birth year and the current year. Calculate and print their age.",
    "3. Simple Calculator (Addition): Prompt the user to enter two numbers. Calculate their sum and display the result.",
    "4. Favorite Color: Ask the user for their favorite color and print a sentence incorporating it.",
    "5. User Details: Ask the user for their first name, last name, and city. Print all the information on separate lines, clearly labeled.",
    "6. Positive, Negative, or Zero: Write a program that takes a number as input and prints whether it's positive, negative, or zero.",
    "7. Even or Odd: Get an integer from the user and determine if it's an even or odd number.",
    "8. Driving Eligibility: Ask the user for their age. If they are 16 or older, print 'You are eligible to drive.' Otherwise, print 'You are not yet eligible to drive.'",
    "9. Grade Classifier: Take a numerical score (0-100) as input. 90-100: Print 'A', 80-89: Print 'B', 70-79: Print 'C', 60-69: Print 'D', Below 60: Print 'F'.",
    "10. Day of the Week: Ask the user to enter a number (1-7). Print the corresponding day of the week (e.g., 1 for Monday). If outside range, print error.",
    "11. Count Up to N: Ask the user for a positive integer N. Use a while loop to print numbers from 1 to N.",
    "12. Countdown: Start a countdown from 10 down to 1 using a while loop, then print 'Blast Off!'.",
    "13. Sum of Numbers (User Input): Prompt the user to enter numbers repeatedly. Stop when the user enters '0'. Print the sum of all entered numbers (excluding '0').",
    "14. Guess the Number: Generate a random number between 1 and 10. Let the user guess. Keep prompting until correct. Give hints.",
    "15. Factorial Calculator: Take a non-negative integer from the user and calculate its factorial using a while loop.",
    "16. Print List Elements: Given a list of fruits ['apple', 'banana', 'cherry'], use a for loop to print each fruit.",
    "17. Sum of List Elements: Given a list of numbers [10, 20, 30, 40, 50], use a for loop to calculate and print their sum.",
    "18. Multiplication Table: Ask the user for a number. Print its multiplication table from 1 to 10 using a for loop.",
    "19. String Reversal: Ask the user for a string. Use a for loop to print the string in reverse order.",
    "20. Count Vowels: Ask the user for a sentence. Use a for loop to count and print the number of vowels (a, e, i, o, u) in the sentence.",
    "21. Basic Addition Function: Write a function `add_numbers(a, b)` that takes two arguments and returns their sum. Call with user inputs.",
    "22. Check Even/Odd Function: Create a function `is_even(number)` that returns True if even, False otherwise. Use it to check a user-provided number.",
    "23. Max of Two Numbers Function: Define a function `find_max(num1, num2)` that returns the larger of the two input numbers.",
    "24. Area of a Rectangle Function: Write a function `calculate_rectangle_area(length, width)` that calculates and returns the area. Get length/width from user.",
    "25. Print Greet Function: Create a function `greet(name='Guest')` that prints 'Hello, [name]!'. Make 'name' optional. Call with/without name.",
    "26. Division by Zero: Ask user for two numbers, perform division. Use try-except to handle `ZeroDivisionError`.",
    "27. Invalid Input (Integer): Prompt user for integer. Use try-except to catch `ValueError` if non-integer. Keep prompting until valid.",
    "28. List Index Out of Range: Create list `my_list = [1, 2, 3]`. Ask user for index. Use try-except to handle `IndexError`.",
    "29. File Not Found: Try to open `non_existent_file.txt` in read mode. Use try-except to catch `FileNotFoundError`.",
    "30. Generic Exception Handling: Write code that might raise errors. Use `except Exception as e:` to catch any error and print message."
]


def assign_questions_to_students():
    """
    Assigns a random exercise to each predefined student,
    and prints the assignments.
    """
    print("Welcome to the Student Question Assigner!")
    print("----------------------------------------")

    # Predefined list of student names
    student_names = ["Jennifer", "Christ", "Truc"]

    if not student_names:
        print("Error: No student names are defined in the list. Please add names to the 'student_names' list.")
        return

    print("\n--- Assigning Questions ---")
    assigned_questions = []

    # Create a copy of the exercises list to draw from,
    # ensuring each question is assigned at most once if there are enough students.
    # If more students than questions, questions will repeat.
    available_exercises = list(EXERCISES)

    for student in student_names:
        if not available_exercises:
            # If all unique questions are assigned, reset available_exercises to allow repetition
            print(f"Warning: Ran out of unique questions. Questions might repeat for {student}.")
            available_exercises = list(EXERCISES)  # Reset to allow questions to be reused

        # Randomly choose an exercise
        chosen_exercise = random.choice(available_exercises)

        # We are allowing repetition, so we don't remove from available_exercises
        # If you wanted strictly unique assignments until all 30 are used, you would uncomment:
        # available_exercises.remove(chosen_exercise)

        assigned_questions.append((student, chosen_exercise))

    print("\n--- Assignments ---")
    for student, question in assigned_questions:
        print(f"Student: {student}\nQuestion: {question}\n")


if __name__ == "__main__":
    assign_questions_to_students()
