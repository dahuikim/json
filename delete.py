import json

file_name = 'employees.json'

with open(file_name,'r', encoding='utf-8') as f:
    load_data = json.load(f)
    print(load_data)

    for name, obj in enumerate(load_data):
        if obj['name']=='김다희':
            load_data.pop(name)

new_file_name = 'new_emplyees.json'

with open(new_file_name,'w',encoding='utf-8') as f:
    f.write(json.dumps(load_data, indent=4, ensure_ascii=False))
    