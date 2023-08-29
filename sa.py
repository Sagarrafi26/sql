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

ui_spec_list = ui_spec.get('identity', {}).get('identity', [])

identity_keys = set(item['id'] for item in ui_spec_list)

for key, value in identity_schema['properties']['identity']['properties'].items():
    if key not in identity_keys:
        result += f"{key} doesn't exist in ui_spec\n"

print(result)
