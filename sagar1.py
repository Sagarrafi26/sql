import json

def find_missing_fields(ui_spec):
    missing_fields = [
        'individualBiometrics',
        'introducerBiometrics',
        'individualAuthBiometrics',
        'UIN',
        'preferredLang',
        'yearOfBirth',
        'monthOfBirth',
        'dayOfBirth'
    ]

    missing_fields_in_ui_spec = []

    for field in missing_fields:
        if field not in ui_spec:
            missing_fields_in_ui_spec.append(field)

    return missing_fields_in_ui_spec

# Load the UI specification from a JSON file
with open('ui_spec_latest.json',encoding='utf-8') as f:
    ui_spec = json.load(f)

missing_fields = find_missing_fields(ui_spec)

for field in missing_fields:
    print(f"{field} doesn't exist in ui_spec")
