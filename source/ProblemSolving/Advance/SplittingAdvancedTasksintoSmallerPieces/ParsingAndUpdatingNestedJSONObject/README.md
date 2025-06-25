You are given a string representation of a nested JSON object. Each JSON object is represented by key-value pairs
enclosed within curly braces {}. Keys and values are separated by colons :, and distinct entries in an object are
separated by commas ,. A value in a JSON object can be a string, a number, or another nested JSON object. For
simplicity, we will not consider arrays or null values in this task.

For example, the string "{\"key1\": \"value1\", \"key2\": {\"key3\": \"value3\", \"key4\": \"value4\"}, \"key5\":
\"value5\"}" represents the following JSON object:

```
{
    "key1": "value1",
    "key2": {
    "key3": "value3",
    "key4": "value4"
    },
    "key5": "value5"
}
```

Your task is to transform the given string into a nested Python dictionary and then update a specific key-value pair
within the dictionary. You should parse the JSON string into a Python dictionary and then update the value associated
with the key "key4" to the given update_value. The string and the new value will be provided as input to your function.
Your function should return the updated dictionary.

The input string will contain from 1 to 500 characters, inclusive. For this task, we'll assume that all keys in the JSON
object are unique.

Example Input: "{\"key1\": \"value1\", \"key2\": {\"key3\": \"value3\", \"key4\": \"value4\"}, \"key5\": \"value5\"}", "
newValue"

Expected Output:

```
{
    "key1": "value1",
    "key2": {
    "key3": "value3",
    "key4": "newValue"
    },
    "key5": "value5"
}
```