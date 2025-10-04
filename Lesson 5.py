def list_validator(check_data):
    if not isinstance(check_data, list):
        raise TypeError(f"Error: got {type(check_data).__name__}, but a list was expected.")
    else:
        return f"List check passed: {check_data}"

user_input = "Hi"
list_validator(user_input)