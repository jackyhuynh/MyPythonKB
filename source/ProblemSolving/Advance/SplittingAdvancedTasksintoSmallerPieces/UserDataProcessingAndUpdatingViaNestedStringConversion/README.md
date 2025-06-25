Imagine that you are a database manager dealing with a data structure in the form of a complex nested string. This
string contains user data and is structured in such a way that user attributes are separated by semicolons (;), and
within each user, the attribute-value pairs are separated by colons (:). Some of the user attributes themselves contain
nested attribute-value pairs, which are enclosed in curly braces ({}).

Here's an example of such a string:

"User1:Age1=21;Location1=USA;Preferences1={Food1=Italian; Sport1=Fencing};User2:Age2=30; Location2=Canada;
Preferences2={Music2=Jazz; Color2=Blue}".

You need to write a Python function that will convert the string into a nested dictionary, following the structure shown
in the string. After the string has been converted into a dictionary, the function should update the value of a
user-preference pair for any user to a requested value and return the updated dictionary.

In this string, the keys representing the user names contain numbers (User1, User2, etc.). You should also provide an
option to find users by their numerical indices following the "User" keyword, such as 1 for User1, 2 for User2, and so
on.

Your function should take the input string, the user index, the preference key, and the new value for the preference
pair, and should return the updated dictionary in the end.

The size of the input string will be less than or equal to 500 characters.

Example:

Input:
input_string: "User1:Age1=21;Location1=USA;Preferences1={Food1=Italian;Sport1=Fencing};User2:
Age2=30;Location2=Canada;Preferences2={Music2=Jazz;Color2=Blue}"
user_index: 1
pref_key: "Sport1"
new_value: "Hockey"

Output:
{
'User1': {'Age1': '21', 'Location1': 'USA', 'Preferences1': {'Food1': 'Italian', 'Sport1': 'Hockey'}},
'User2': {'Age2': '30', 'Location2': 'Canada', 'Preferences2': {'Music2': 'Jazz', 'Color2': 'Blue'}}
}
