student={
    "101":{"name":"rahul","age":14,"grade":"B"},
    "102":{"name":"anitha","age":15,"grade":"A"}
}

print(student["102"]["name"])

student["101"]["grade"]="A+"

print(student)

student["103"]={"name":"vikram","age":"16","grade":"B+"}

print(student)

result={i:student[i]["name"] for i in student}

print(result)


