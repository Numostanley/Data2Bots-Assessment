from schema_sniffer import SchemaSniffer

def main() -> None:
    
    # create a list of input data and schema files
    input_data = ['data/data_1.json', 'data/data_2.json']
    input_schemas = ['schema/schema_1.json', 'schema/schema_2.json']

    # iterate through the list and process each data and schema file
    for i, (data_file, schema_file) in enumerate(zip(input_data, input_schemas)):
        schema = SchemaSniffer(data_file, schema_file)
        data = schema.read_input_file()
        schema.sniff_schema(data=data)
        schema.write_output()
        
if __name__ == '__main__':
    main()
