import unittest

from solution import solution


class SolutionTest(unittest.TestCase):
    def test_1(self):
        string_input = "User1:Age1=21;Location1=USA;Preferences1={Food1=Italian;Sport1=Fencing};User2:Age2=30;Location2=Canada;Preferences2={Music2=Jazz;Color2=Blue}"
        user_index = 1
        pref_key = "Sport1"
        new_value = "Hockey"
        expected_output = {
            'User1': {'Age1': '21', 'Location1': 'USA', 'Preferences1': {'Food1': 'Italian', 'Sport1': new_value}},
            'User2': {'Age2': '30', 'Location2': 'Canada', 'Preferences2': {'Music2': 'Jazz', 'Color2': 'Blue'}}
        }
        result = solution(string_input, user_index, pref_key, new_value)
        self.assertDictEqual(result, expected_output)

    def test_2(self):
        string_input = "User1:Age1=21;Location1=USA;Preferences1={Food1=Italian;Sport1=Fencing}"
        user_index = 1
        pref_key = "Sport1"
        new_value = "Football"
        expected_output = {
            'User1': {'Age1': '21', 'Location1': 'USA', 'Preferences1': {'Food1': 'Italian', 'Sport1': new_value}}
        }
        result = solution(string_input, user_index, pref_key, new_value)
        self.assertDictEqual(result, expected_output)

    def test_3(self):
        string_input = "User1:Age1=45;Location1=UK;Preferences1={Food1=Asian;Sport1=Golf};User2:Age2=22;Location2=Africa;Preferences2={Music2=Reggae;Color2=Yellow}"
        user_index = 2
        pref_key = "Color2"
        new_value = "Purple"
        expected_output = {
            'User1': {'Age1': '45', 'Location1': 'UK', 'Preferences1': {'Food1': 'Asian', 'Sport1': 'Golf'}},
            'User2': {'Age2': '22', 'Location2': 'Africa', 'Preferences2': {'Music2': 'Reggae', 'Color2': new_value}}
        }
        result = solution(string_input, user_index, pref_key, new_value)
        self.assertDictEqual(result, expected_output)

    def test_4(self):
        string_input = "User1:Age1=65;Location1=Australia;Preferences1={Food1=Seafood;Sport1=Surfing}"
        user_index = 1
        pref_key = "Food1"
        new_value = "Thai"
        expected_output = {
            'User1': {'Age1': '65', 'Location1': 'Australia', 'Preferences1': {'Food1': new_value, 'Sport1': 'Surfing'}}
        }
        result = solution(string_input, user_index, pref_key, new_value)
        self.assertDictEqual(result, expected_output)

    def test_5(self):
        string_input = "User1:Age1=30;Location1=Germany;Preferences1={Food1=Bavarian;Sport1=Football};User2:Age2=25;Location2=India;Preferences2={Music2=Classical;Color2=Violet}"
        user_index = 2
        pref_key = "Music2"
        new_value = "Pop"
        expected_output = {
            'User1': {'Age1': '30', 'Location1': 'Germany',
                      'Preferences1': {'Food1': 'Bavarian', 'Sport1': 'Football'}},
            'User2': {'Age2': '25', 'Location2': 'India', 'Preferences2': {'Music2': new_value, 'Color2': 'Violet'}}
        }
        result = solution(string_input, user_index, pref_key, new_value)
        self.assertDictEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()
