file_path="task-nutristion-3-12-25\\Food_Nutrition_Dataset.csv.xls"
fr = open(file_path,"r",encoding="utf-8")

import csv

reader=csv.DictReader(fr)

data=[row for row in reader]

# print(data)

five_row=[r for r in data][:5]

# print(five_row)

# which food have maximum protien contant

food_protien={r.get("food_name"):r.get("protein") for r in data}

max_protien=[k for k,v in food_protien.items() if v==max(food_protien.values())]

# print(max_protien)

# which food have height carb

food_carbs={r.get("food_name"):r.get("carbs") for r in data}

max_carb=[k for k,v in food_carbs.items() if v==max(food_carbs.values())]

# print(max_carb)

# Calculate average calories of all foods

all_calories=[float(r.get("calories")) for r in data]

avg_calorie=sum(all_calories)/len(all_calories)

# print(avg_calorie)

#Filter foods with vitamin C > 10mg

fd_vitamin_c=[r.get("food_name") for r in data if float(r.get("vitamin_c") or 0)>10]

# print(fd_vitamin_c)


#  variety of apple foods

food_apple=[r.get("food_name") for r in data if r.get("category")=="Apples"]

# print(food_apple)

"""
Q.Create a healthy-food filter

Criteria example:
calories < 150
fat < 5
vitamin C > 3
"""

healthy_food=[]

for r in data:
    if float(r.get("calories"))< 100 and float(r.get("fat"))<5 and float(r.get("vitamin_c") or 0)>3:
        healthy_food.append(r.get("food_name"))

print(healthy_food)



