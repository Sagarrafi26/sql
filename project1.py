import json

with open('id_schema_latest.json', encoding='utf-8') as f:
    identity_schema = json.load(f)

with open('ui_spec_latest.json', encoding='utf-8') as f:
    ui_spec = json.load(f)

schema_properties = identity_schema.get('properties', {}).get('identity', {}).get('properties', {})
missing_keys = []

for key in schema_properties:
    if key not in ui_spec.get("identity", {}).get("identity", {}):
        missing_keys.append(f"{key} doesn't exist in ui_spec")

missing_values = []
for key in missing_keys:
    missing_value = schema_properties.get(key)
    missing_values.append(f"{key}: {missing_value}")

result = "\n".join(missing_values)
print(result)
