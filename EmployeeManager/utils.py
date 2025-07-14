def get_input(prompt, cast_type=str, allow_empty=False):
    while True:
        value = input(prompt)
        if not value and allow_empty:
            return None
        try:
            return cast_type(value)
        except ValueError:
            print(f"Invalid input. Please enter a valid {cast_type.__name__}.")