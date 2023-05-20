import json

class JsonSchemaGenerator:
    def __init__(self, file_path):
        self.file_path = file_path
        self.json_data = None
        self.schema = {}

    def read_json_file(self):
        with open(self.file_path) as file:
            self.json_data = json.load(file)
            # print(self.json_data)

    def generate_json_schema(self):
        self._process_object(self.json_data["message"], self.schema)

    def _process_object(self, obj, schema_obj):
        for key, value in obj.items():
            if isinstance(value, str):
                schema_obj[key] = self._map_string(value)
            elif isinstance(value, bool):
                schema_obj[key] = self._map_bool(value)
            elif isinstance(value, int):
                schema_obj[key] = self._map_integer(value)
            elif isinstance(value, dict):
                schema_obj[key] = self._map_object(value)
            elif isinstance(value, list):
                if value and isinstance(value[0], str):
                    schema_obj[key] = self._map_enum(value)
                elif value and isinstance(value[0], dict):
                    schema_obj[key] = self._map_array(value[0])


    def _map_string(self, value):
        return {
            "type": "string",
            "tag": "",
            "description": "",
            "required": False
        }

    def _map_integer(self, value):
        return {
            "type": "integer",
            "tag": "",
            "description": "",
            "required": False
        }

    def _map_enum(self, value):
        return {
            "type": "enum",
            "tag": "",
            "description": "",
            "required": False
        }

    def _map_array(self, value):
        return {
            "type": "array",
            "items": self._map_object(value),
            "tag": "",
            "description": "",
            "required": False
        }

    def _map_object(self, value):
        schema_obj = {
            "type": "object",
            "properties": {},
            "tag": "",
            "description": "",
            "required": False
        }
        self._process_object(value, schema_obj["properties"])
        return schema_obj
    
    def _map_bool(self, value):
        return {
            "type": "boolean",
            "tag": "",
            "description": "",
            "required": False
        }

    def dump_schema(self, output_file):
        with open(output_file, "w") as file:
            json.dump(self.schema, file, indent=2)

# Usage example
file_path = "./data/data_2.json"  # Replace with the actual file path

sniffer = JsonSchemaGenerator(file_path)
sniffer.read_json_file()
sniffer.generate_json_schema()
sniffer.dump_schema("./schema/schema_2.json")
