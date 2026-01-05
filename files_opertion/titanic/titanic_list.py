file_path="files_opertion\\titanic\\data_set.csv"

fr=open(file_path,"r")

import csv

reader=csv.DictReader(fr)

data=[row for row in reader]

# print(data)

name=[r.get("Name") for r in data ]

# print(name)

gender=[r.get("Sex") for r in data]   # we got list of gender

# male count & female count

male_count=gender.count("male")
female_count=gender.count("female")

# print("male count=",male_count)
# print("female count=",female_count)

unsurvived_survived=[r.get("Survived") for r in data]

# print("survived",unsurvived_survived.count("1"))
# print("unsurvived",unsurvived_survived.count("0"))

genders1=[p.get("Sex") for p in data]

# print("male_count=",genders1.count("male"))
# print("female_count=",genders1.count("female"))

all_class=[p.get("Pclass") for p in data]

class_count={c:c.count(c) for c in all_class}

# print(class_count)

age=[int(a.get("Age")) for a in data if a.get("Age").isdigit()]

min_age=min(age)
max_age=max(age)

# print(min_age)
# print(max_age)

younget=[]

# print("youngest=",)
# print("oldest=",)

#number of pasenger boarding fromm each station


boarding_station=[p.get("Embarked") for p in data if len(p.get("Embarked"))>0]

bc={s:boarding_station.count(s) for s in boarding_station}

# print(bc)

# age_pass=[age.get("Age") for age in data ]

# pass_below_ten=[a for a in age_pass if a.isdigit() and int(a)< 10 ]

# print(len(pass_below_ten))

children=[p for p in data if p.get("Age").isdigit()and int(p.get("Age"))<10]

# print(len(children))

survived=[p for p in children if p.get("Survived")=="1"]
# print("survived children",len(survived))

# calculate survival rate

survived_count=([p for p in data if p.get("Survived")=="1"])

rate_of_survived=(len(survived_count)/len(name))*100

# print(rate_of_survived)



total_male=[ m for m in  data if m.get("Sex")=="male"]

male_surv=[p for p in  total_male if p.get("Survived")=="1" ]

rate_male_survive=(len(male_surv)/len(total_male))*100
# print(rate_male_survive)

total_female=[ f for f in  data if f.get("Sex")=="female"]

fem_survived=[p for p in total_female if p.get("Survived")=="1"]

rate_female_survived=(len(fem_survived)/len(total_female))*100

# print(rate_female_survived)

all_p_class=[p.get("Pclass") for p in data]
class_count={c:all_p_class.count(c) for c in all_p_class}
print(class_count)

all_p_class_survived=[p.get("Pclass") for p in data if p.get("Survived")=="1"]

class_survived_count={c:all_p_class_survived.count(c) for c in all_p_class_survived}

print(class_survived_count)

for k,v in class_count.items():

    s_p=class_survived_count.get(k)

    rate=(s_p/v)*100

    print(k,"=",rate)



















