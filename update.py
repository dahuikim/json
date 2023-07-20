import json
employee ='{"name":김다희, "email":"kimda@", "age": 25, "position": "대리"}'
insert_obj = {"emp_id":"asd"}

employee_dict = json.loads(employee)

employee_dict.update(insert_obj)
print(json.dump(employee_dict, indent=4, ensure_ascii=False))
