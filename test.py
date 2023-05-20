import unittest, json, os
from main import JsonSchemaGenerator

class JsonSchemaGeneratorTest_1(unittest.TestCase):
    def setUp(self):
        self.json_file_path = "./data/data_1.json"  

    def test_read_json_file(self):
        generator = JsonSchemaGenerator(self.json_file_path)
        generator.read_json_file()

        self.assertIsNotNone(generator.json_data)
        self.assertIsInstance(generator.json_data, dict)

    def test_json_schema(self):
        generator = JsonSchemaGenerator(self.json_file_path)
        generator.read_json_file()
        generator.generate_json_schema()

        self.assertIsNotNone(generator.schema)
        self.assertIsInstance(generator.schema, dict)

        # Additional assertions to check the structure of the generated schema
        self.assertIn("battle", generator.schema)
        self.assertIn("id", generator.schema["battle"]["properties"])
        self.assertIn("name", generator.schema["battle"]["properties"])
        self.assertIn("settings", generator.schema["battle"]["properties"])
        self.assertIn("minParticipants", generator.schema["battle"]["properties"]["settings"]["properties"])
        self.assertIn("participants", generator.schema["battle"]["properties"])

        # Verify the data type mappings
        self.assertEqual(generator.schema["battle"]["properties"]["id"]["type"], "string")
        self.assertEqual(generator.schema["battle"]["properties"]["name"]["type"], "string")
        self.assertEqual(generator.schema["battle"]["properties"]["settings"]["type"], "object")
        self.assertEqual(generator.schema["battle"]["properties"]["settings"]["properties"]["minParticipants"]["type"], "integer")
        self.assertEqual(generator.schema["battle"]["properties"]["participants"]["type"], "array")

    def test_dump_schema(self):
        output_file = "./schema/schema_1.json"  

        generator = JsonSchemaGenerator(self.json_file_path)
        generator.read_json_file()
        generator.generate_json_schema()
        generator.dump_schema(output_file)

        # Verify that the output file exists
        self.assertTrue(os.path.exists(output_file))

        # Additional assertions to validate the content of the output file
        with open(output_file) as file:
            schema_data = json.load(file)

        self.assertIsInstance(schema_data, dict)
        self.assertIn("battle", schema_data)
        self.assertIn("id", schema_data["battle"]["properties"])
        self.assertIn("name", schema_data["battle"]["properties"])
        self.assertIn("settings", schema_data["battle"]["properties"])
        self.assertIn("minParticipants", schema_data["battle"]["properties"]["settings"]["properties"])
        self.assertIn("participants", schema_data["battle"]["properties"])

        # Verify the data type mappings in the output schema
        self.assertEqual(schema_data["battle"]["properties"]["id"]["type"], "string")
        self.assertEqual(schema_data["battle"]["properties"]["name"]["type"], "string")
        self.assertEqual(schema_data["battle"]["properties"]["settings"]["type"], "object")
        self.assertEqual(schema_data["battle"]["properties"]["settings"]["properties"]["minParticipants"]["type"], "integer")
        self.assertEqual(schema_data["battle"]["properties"]["participants"]["type"], "array")

class JsonSchemaGeneratorTest_2(unittest.TestCase):
    def setUp(self):
        self.json_file_path = "./data/data_2.json"  

    def test_read_json_file(self):
        generator = JsonSchemaGenerator(self.json_file_path)
        generator.read_json_file()

        self.assertIsNotNone(generator.json_data)
        self.assertIsInstance(generator.json_data, dict)

    def test_json_schema(self):
        generator = JsonSchemaGenerator(self.json_file_path)
        generator.read_json_file()
        generator.generate_json_schema()

        self.assertIsNotNone(generator.schema)
        self.assertIsInstance(generator.schema, dict)

        # Additional assertions to check the structure of the generated schema
        self.assertIn("user", generator.schema)
        self.assertIn("id", generator.schema["user"]["properties"])
        self.assertIn("nickname", generator.schema["user"]["properties"])
        self.assertIn("countryCode", generator.schema["user"]["properties"])
        self.assertIn("time", generator.schema)
        self.assertIn("publicFeed", generator.schema)

        # Verify the data type mappings
        self.assertEqual(generator.schema["user"]["properties"]["id"]["type"], "string")
        self.assertEqual(generator.schema["user"]["properties"]["nickname"]["type"], "string")
        self.assertEqual(generator.schema["user"]["properties"]["countryCode"]["type"], "string")
        self.assertEqual(generator.schema["time"]["type"], "integer")
        self.assertEqual(generator.schema["internationalCountries"]["type"], "enum")
        self.assertEqual(generator.schema["publicFeed"]["type"], "boolean")

    def test_dump_schema(self):
        output_file = "./schema/schema_2.json"  

        generator = JsonSchemaGenerator(self.json_file_path)
        generator.read_json_file()
        generator.generate_json_schema()
        generator.dump_schema(output_file)

        # Verify that the output file exists
        self.assertTrue(os.path.exists(output_file))

        # Additional assertions to validate the content of the output file
        with open(output_file) as file:
            schema_data = json.load(file)

        self.assertIsInstance(schema_data, dict)
        self.assertIn("user", schema_data)
        self.assertIn("id", schema_data["user"]["properties"])
        self.assertIn("nickname", schema_data["user"]["properties"])
        self.assertIn("countryCode", schema_data["user"]["properties"])
        self.assertIn("time", schema_data)
        self.assertIn("publicFeed", schema_data)

        # Verify the data type mappings in the output schema
        self.assertEqual(schema_data["user"]["properties"]["id"]["type"], "string")
        self.assertEqual(schema_data["user"]["properties"]["nickname"]["type"], "string")
        self.assertEqual(schema_data["user"]["properties"]["countryCode"]["type"], "string")
        self.assertEqual(schema_data["time"]["type"], "integer")
        self.assertEqual(schema_data["internationalCountries"]["type"], "enum")
        self.assertEqual(schema_data["publicFeed"]["type"], "boolean")

if __name__ == "__main__":
    unittest.main()
