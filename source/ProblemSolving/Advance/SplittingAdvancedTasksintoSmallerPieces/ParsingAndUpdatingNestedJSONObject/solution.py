def solution(json_string, update_value):
    """
    Input: "{\"key1\": \"value1\", \"key2\": {\"key3\": \"value3\", \"key4\": \"value4\"}, \"key5\": \"value5\"}"
    Output:
    {
        "key1": "value1",
        "key2": {
            "key3": "value3",
            "key4": "value4"
        },
        "key5": "value5"
    }
    """

    def parse_json(json_string):
        import json
        try:
            return json.loads(json_string)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON string: {e}")

    def update_json(json_obj, update_value):
        for key, value in json_obj.items():
            if key == "key4":
                json_obj[key] = update_value
            if isinstance(value, dict):
                update_json(value, update_value)

    json_obj = parse_json(json_string)
    update_json(json_obj, update_value)
    return json_obj
