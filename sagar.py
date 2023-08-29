import json
import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))

with open('id_schema_latest.json', encoding='utf-8') as f:
    json_data = f.read()

identity_schema = json.loads(json_data)

os.chdir(os.path.dirname(os.path.realpath(__file__)))

with open('ui_spec_latest.json', encoding='utf-8') as f:
    json_data = f.read()

ui_spec = json.loads(json_data)

result = ""

ui_identity = ui_spec.get('identity', {}).get('identity', {})


for key, value in identity_schema['properties']['identity']['properties'].items():
    if value.get('value') not in ui_identity:
        #result += f"{key} doesn't exist in ui_spec\n"
        result += f"For {key} in identity_schema value: {key} is missing from identity_schema\n"

print(result)


'''for key, value in identity_mapping['identity'].items():

    if value.get('value') not in identity_properties:

        result += f"For {key} in identity_mapping value: {value} is missing from identity_schema\n"




result1 = "_______________________metaInfo object_________________________\n"'''