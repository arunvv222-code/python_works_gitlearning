from json import load

file_path="json_works\\student.json"

fr=open(file_path,"r",encoding="utf-8")

data=load(fr) # convert json to python native type

# for st in data:
#     # print(st.get("name"))

result=[r.get("name") for r in data if r.get("course")=="testing"]

# print(result)

