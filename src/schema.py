def get_schema(data: dict) -> dict:
    # Initialize empty dictionary for schema
    schema = {}

    # Iterate through keys and values in data
    for key, value in data.items():
        # Initialize empty dictionary for a current key in schema
        attributes = {}

        # If value is a bool, set type to bool
        if isinstance(value, bool):
            attributes['type'] = 'boolean'
        # If value is a string, set type to string
        elif isinstance(value, str):
            attributes['type'] = 'string'
        # If value is an integer, set type to integer
        elif isinstance(value, int):
            attributes['type'] = 'integer'
        # If value is a dictionary, set type to object and recursively call get_schema
        elif isinstance(value, dict):
            attributes['type'] = 'object'
            attributes['properties'] = get_schema(value)
        # If value is a list
        elif isinstance(value, list):
            try:
                # If a first element in a list is a string, set type to array of strings (enum)
                if isinstance(value[0], str):
                    attributes['type'] = 'enum'
                    attributes['items'] = {'type': 'string'}
                # If a first element in a list is a dictionary,
                # set type to array of objects and recursively call get_schema
                elif isinstance(value[0], dict):
                    attributes['type'] = 'array'
                    attributes['items'] = {'type': 'object', 'properties': get_schema(value[0])}
            # if the list is empy
            except IndexError:
                attributes['type'] = "list"

        # Add padding to attributes.
        attributes['tag'] = key.capitalize()
        if (isinstance(value, bool)) or (isinstance(value, str)) or (isinstance(value, int)):
            attributes['description'] = f"The {key.capitalize()} attribute. Represented as {value}"
        else:
            attributes['description'] = f"The {key.capitalize()} attribute. Represented by a(n) {attributes['type']} data type."

        # Set the required key to false
        attributes['required'] = False

        # Set the current attribute to its respective key.
        schema[key] = attributes

    # Return schema
    return schema
