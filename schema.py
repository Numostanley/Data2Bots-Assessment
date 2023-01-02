def get_schema(data: dict) -> dict:
    # Initialize empty dictionary for schema
    schema = {}

    # Iterate through keys and values in message
    for key, value in data.items():
        # Initialize empty dictionary for current key in schema
        attributes = {}
        # Set required key to false
        attributes['required'] = False
        
        # If value is a bool, set type to bool
        if type(value) == bool:
            attributes['type'] = 'bool'
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
                # If first element in list is a string, set type to array of strings (enum)
                if isinstance(value[0], str):
                    attributes['type'] = 'enum'
                    attributes['items'] = {'type': 'string'}
                # If first element in list is a dictionary, set type to array of objects and recursively call get_schema
                elif isinstance(value[0], dict):
                    attributes['type'] = 'array'
                    attributes['items'] = {'type': 'object', 'properties': get_schema(value[0])}
            except IndexError:
                attributes['type'] = "list"
                   
        # Set current key in schema to attributes
        schema[key] = attributes

    # Return schema
    return schema
