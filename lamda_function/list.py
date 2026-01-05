employee=[
    ["sam",10000,4],
    ["akash",250000,3],
    ["ravi",35000,2],
    ["arun",100000,6],
    ["saniya",30000,5]
]

employee_year=sorted(employee,key=lambda lst :lst[2])

# print(employee_year)

employe_salary=sorted(employee,key=lambda n : n[1])

print(employe_salary)