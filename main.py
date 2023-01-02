from schema_sniffer import SchemaSniffer

def main() -> None:
    
    schema_1 = SchemaSniffer('data/data_1.json', 'schema/schema_1.json')
    data_1= schema_1.read_input_file()
    schema_1.sniff_schema(data=data_1)
    schema_1.add_padding()
    schema_1.write_output()
    
    schema_2 = SchemaSniffer('data/data_2.json', 'schema/schema_2.json')
    data_2 = schema_2.read_input_file()
    schema_2.sniff_schema(data=data_2)
    schema_2.add_padding()
    schema_2.write_output()
    
if __name__ == '__main__':
    main()
