employees = {
"E01": {"name": "Arjun", "dept": "HR"},
"E02": {"name": "Sara", "dept": "IT"},
"E03": {"name": "Manoj", "dept": "Finance"}
}

employees["E01"]["dept"]="admin"

print(employees)

employees["E04"]={"name": "lakshmi", "dept": "marketing"}

print(employees)

emp_name=[employees[i]["name"] for i in employees]

print(emp_name)

