import unittest

from solution import solution


class SolutionTests(unittest.TestCase):
    def test1(self):
        input_data = (
            "{\"key1\": \"value1\", \"key2\": {\"key3\": \"value3\", \"key4\": \"value4\"}, \"key5\": \"value5\"}",
            "newValue")
        expected_output = {'key1': 'value1', 'key2': {'key3': 'value3', 'key4': 'newValue'}, 'key5': 'value5'}
        self.assertEqual(solution(*input_data), expected_output)

    def test2(self):
        input_data = ("{\"key1\": \"value1\", \"key2\": {\"key3\": \"value3\", \"key4\": \"value4\"}}", "testValue")
        expected_output = {'key1': 'value1', 'key2': {'key3': 'value3', 'key4': 'testValue'}}
        self.assertEqual(solution(*input_data), expected_output)

    def test3(self):
        input_data = ("{\"key4\": \"value4\"}", "newValue")
        expected_output = {'key4': 'newValue'}
        self.assertEqual(solution(*input_data), expected_output)

    def test4(self):
        input_data = ("{\"key1\": {\"key2\": {\"key3\": {\"key4\": \"value4\"}}}}", "deepValue")
        expected_output = {'key1': {'key2': {'key3': {'key4': 'deepValue'}}}}
        self.assertEqual(solution(*input_data), expected_output)

    def test5(self):
        input_data = ("{\"key1\": {\"key3\": \"value3\", \"key4\": \"value4\"}, \"key2\": \"value2\"}", "topLevelValue")
        expected_output = {'key1': {'key3': 'value3', 'key4': 'topLevelValue'}, 'key2': 'value2'}
        self.assertEqual(solution(*input_data), expected_output)


if __name__ == '__main__':
    unittest.main()
