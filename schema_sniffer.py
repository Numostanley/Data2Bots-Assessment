import json
from dataclasses import dataclass, field


@dataclass
class SchemaSniffer:
    """Reads a json input file, sniffs the schema of the json file,  
    and writes the output to a json file."""
    
    __input_file: str
    __output_file: str
    __schema: dict[str, dict] = field(default_factory=dict)

    def read_input_file(self) -> dict:
        """read the JSON file"""

        with open(self.__input_file, 'r') as f:
            data = json.load(f)
        return data
            
    def sniff_schema(self, data: dict) -> None:
        """sniffs the schema of the JSON file"""
        
        for key, value in data['message'].items():
            schema = {"type": "", "tag": "", "description": "", "required": False}
            
            if isinstance(value, str):
                schema["type"] = "string"
            elif isinstance(value, int):
                schema["type"] = "integer"
            elif isinstance(value, list):
                try:
                    if isinstance(value[0], str):
                        schema["type"] = "enum"
                    elif isinstance(value[0], dict):
                        schema["type"] = "array"
                except IndexError:
                    schema["type"] = "array"
                    schema["description"] = "Empty list"
            elif isinstance(value, dict):
                schema["type"] = "json_object"
            
            self.__schema[key] = schema

    def write_output(self) -> None:
        # dump the output in the schema.json
        output = json.dumps(self.__schema, indent=4)
        with open(self.__output_file, 'w') as f:
            f.write(output)
