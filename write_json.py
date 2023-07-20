import json

employee_dict = {
    "name":"김다희",
    "email":"acd",
    "age":25,
    "position":"대리"

}

print(type(employee_dict))

json_object = json.dumps(employee_dict, indent=4, ensure_ascii=False)
print(json_object)

employee_dict = {
    "name":"김다희",
    "email":"acd",
    "age":25,
    "position":"대리"
}

print(type(employee_dict))

with open("employees.json","w",encoding='utf-8') as outfile:
    json.dump(employee_dict, outfile, ensure_ascii=False)




