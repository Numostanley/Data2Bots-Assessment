from unittest import TestCase, main
import json

from schema_sniffer import SchemaSniffer


class TestSchemaSniffer(TestCase):
    
    def setUp(self) -> None:
        self.sniffer = SchemaSniffer('data/data_2.json', 'schema/schema_2.json')
        self.data = self.sniffer.read_input_file()
        self.sniffer.sniff_schema(data=self.data)
        self.sniffer.add_padding()
        self.sniffer.write_output()
        with open('schema/schema_2.json', 'r') as f:
            self.output = json.load(f)
    
    def test_read_input_file(self) -> None:
        self.assertIn('message', self.data)
        self.assertEqual(type(self.data), dict)
        self.assertEqual(type(self.data['message']), dict)
    
    def test_output(self) -> None:
        self.assertEqual(type(self.output), dict)
        for item in self.output.values():
            self.assertIn('tag', item)
            self.assertIn('type', item)
            self.assertIn('description', item)
            self.assertIn('required', item)

if __name__ == '__main__':
    main()
