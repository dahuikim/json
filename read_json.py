# import json
# employee = '{"name":"김", "email": kim@gmail.com, "age":25, "position":"대리"}'

# employee_dict = json.loads(employee)
# print(type(employee_dict))

# print(employee_dict)

load_file = open('employees.json',encoding='utf-8')

data = json.load(load_file)

for item in data:
    print(item)

load_file.close()