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

ui_identity = ui_spec.get('identity', {})
ui_identity_list = ui_identity.get('identity', {}).keys()

for key, value in identity_schema['properties']['identity']['properties'].items():
    if key not in ui_identity_list:
        result += f"{key} doesn't exist in ui_spec\n"

print(result)


