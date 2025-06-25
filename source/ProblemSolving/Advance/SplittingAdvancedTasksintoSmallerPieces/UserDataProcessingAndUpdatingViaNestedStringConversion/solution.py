import re


def solution(input_string, user_index, pref_key, new_value):
    '''
    Input:
        input_string: "User1:Age1=21;Location1=USA;Preferences1={Food1=Italian;Sport1=Fencing};User2:Age2=30;Location2=Canada;Preferences2={Music2=Jazz;Color2=Blue}"
        user_index: 1
        pref_key: "Sport1"
        new_value: "Hockey"

    Output
    {
        'User1': {'Age1': '21', 'Location1': 'USA', 'Preferences1': {'Food1': 'Italian', 'Sport1': 'Hockey'}},
        'User2': {'Age2': '30', 'Location2': 'Canada', 'Preferences2': {'Music2': 'Jazz', 'Color2': 'Blue'}}
    }
    '''

    def parse_preferences(pref_string):
        """
        Parses a preference string like "Food1=Italian;Sport1=Fencing" into a dictionary.
        """
        preferences = {}
        # Split by semicolon, but only if not inside curly braces (though not strictly needed for this level)
        pref_parts = re.split(r';', pref_string)
        for part in pref_parts:
            part = part.strip()
            if '=' in part:
                key, value = part.split('=', 1)
                preferences[key.strip()] = value.strip()
        return preferences

    def convert_array_to_dict(input_array_of_strings):
        """
        Converts an array of strings (representing user attributes) into a dictionary.

        Args:
            input_array_of_strings: A list of strings, where each string is a key-value pair.
                                    Example: ['Age1=21', 'Location1=USA', 'Preferences1={Food1=Italian;Sport1=Fencing}']

        Returns:
            A dictionary representing the parsed user data.
            Example: {'Age1': '21', 'Location1': 'USA', 'Preferences1': {'Food1': 'Italian', 'Sport1': 'Fencing'}}
        """
        user_data = {}
        for item_string in input_array_of_strings:
            item_string = item_string.strip()
            if '=' in item_string:
                key, value = item_string.split('=', 1)
                key = key.strip()
                value = value.strip()

                if value.startswith('{') and value.endswith('}'):
                    # This is a preferences block, so parse it into another dictionary
                    user_data[key] = parse_preferences(value[1:-1])
                else:
                    user_data[key] = value
        return user_data

    def update_data(dictionary, pref_key, update_value):
        for key, value in dictionary.items():
            if key == pref_key:
                dictionary[key] = update_value
                return
            if isinstance(value, dict):
                update_data(value, pref_key, update_value)

    users = {}
    user_blocks = re.split(r'(User\d+):', input_string)

    for i in range(1, len(user_blocks), 2):
        user_name = user_blocks[i]
        user_data_string = user_blocks[i + 1]
        data_parts = re.split(r';(?![^{]*})', user_data_string)
        data_parts = [item for item in data_parts if item]
        users[user_name] = convert_array_to_dict(data_parts)

    user_key = f"User{user_index}"
    update_data(users[user_key], pref_key, new_value)

    return users
