file_path="task-27-11-25_fop\\python_basics_report.csv"

fr=open(file_path,"r")



import csv

reader=csv.DictReader(fr)

data=[row for row in reader]

# print (data)

#Count Total Students Count how many students are in the dataset.

# print(len(data))

# Print only the Name column for all students.

names=[r.get("NAME") for r in data]

# print(names)

# Print all students whose BATCH = "Python".

st_python=[r.get("NAME") for r in data if r.get("BATCH ")=="Python"]

# print(st_python)

# Print names of students whose PRESENT_% = 100

st_present=[r.get("NAME") for r in data if float(r.get("PRESENT_%") or 0)==100]

# print(st_present)

#Print only names and MCQ1 values.

names_MCQ1={r.get("NAME"):r.get("MCQ1") for r in data}

# print(names_MCQ1)


# Find Student With Highest OVERALL
# Print the name and OVERALL% of the top 


student_overall={r.get("NAME"): r.get("OVERALL") for r in data}

max_overall={k:v for k,v in student_overall.items() if v== max(student_overall.values())}

# print(max_overall)

#Print students whose OVERALL < 30%.

overall_lessthan_thirty={k:v for k,v in student_overall.items() if v<"30"}

print(overall_lessthan_thirty)