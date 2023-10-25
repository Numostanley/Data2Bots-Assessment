from unittest import TestCase, main
import json

from src.schema_sniffer import SchemaSniffer


class TestSchemaSniffer(TestCase):
    """Test class for the SchemaSniffer class."""
    
    def setUp(self) -> None:
        """Set up the test environment by creating a SchemaSniffer object and reading the input file."""
        self.sniffer = SchemaSniffer('data/data_2.json', 'schema/schema_2.json')
        self.data = self.sniffer.read_input_file()
        self.sniffer.sniff_schema(data=self.data)
        self.sniffer.write_output()
        with open('schema/schema_2.json', 'r') as f:
            self.output = json.load(f)
    
    def test_read_input_file(self) -> None:
        """Test that the input file is correctly read and the data is correctly parsed."""
        self.assertIsInstance(self.data, dict)
        self.assertIn('message', self.data)
        self.assertIsInstance(self.data['message'], dict)
    
    def test_sniff_schema(self) -> None:
        """Test that the schema is correctly sniffed and written to the output file."""
        self.assertIsInstance(self.output, dict)
        for item in self.output.values():
            self.assertIn('tag', item)
            self.assertIn('type', item)
            self.assertIn('description', item)
            self.assertIn('required', item)
            
    def test_invalid_input_file(self) -> None:
        """Test that an exception is raised when an invalid input file is provided."""
        with self.assertRaises(FileNotFoundError):
            sniffer = SchemaSniffer('invalid/path.json', '../schema/schema_2.json')
            sniffer.read_input_file()
    
    def test_invalid_schema_file(self) -> None:
        """Test that an exception is raised when an invalid schema file is provided."""
        with self.assertRaises(FileNotFoundError):
            sniffer = SchemaSniffer('data/data_2.json', 'invalid/path.json')
            data = self.sniffer.read_input_file()
            sniffer.sniff_schema(data=data)
            sniffer.write_output()


if __name__ == '__main__':
    main()
