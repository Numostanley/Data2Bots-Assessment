import json
from dataclasses import dataclass, field
from typing import Callable

from schema import get_schema


@dataclass
class SchemaSniffer:
    """Reads a json input file, sniffs the schema of the json file,
    and writes the output to a json file."""
    
    __input_file: str
    __output_file: str
    __schema: dict[str, dict] = field(default_factory=dict)
    sniffer: Callable[[dict], dict] = get_schema

    def read_input_file(self) -> dict:
        """read the JSON file"""

        with open(self.__input_file, 'r') as f:
            data = json.loads(f.read())
        return data
            
    def sniff_schema(self, data: dict) -> None:
        """sniffs the schema of the JSON file"""
        
        # get only the attributes within the "message" key
        data_items = data['message']
        self.__schema = self.sniffer(data_items)

    def write_output(self) -> None:
        # dump the output in the schema.json
        output = json.dumps(self.__schema, indent=3)
        with open(self.__output_file, 'w') as f:
            f.write(output)
