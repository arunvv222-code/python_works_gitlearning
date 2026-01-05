file_path="task-5-1-25-country\\country_wise_latest_covid.csv"

fr=open(file_path,"r")

import csv

reader=csv.DictReader(fr)

data=[row for row in reader]
#1
#print(len(data))

#2 whic country has heightest number of new case

new_cases=[int(r.get("New cases")) for r in data]

country_highest_new_cases={r.get("Country/Region"):int(r.get("New cases")) for r in data if int(r.get("New cases"))== max(new_cases)}

# print(country_highest_new_cases)

#3 countrys with who region is america

country=[r.get("Country/Region") for r in data if r.get("WHO Region")=="Americas"]

# print(country)

#4 which country has height number of death 

death=[int(r.get("Deaths")) for r in data]

country_height_death={r.get("Country/Region"):r.get("Deaths") for r in data if int(r.get("Deaths"))==max(death)}

# print(country_height_death)

#5 total number of death occured

# print(sum(death))

#6 average number of new deaths

average_death=sum(death)/len(death)

# print(average_death)

#7number of recovered patients from who region europe

recovered_patients=[int(r.get("Recovered")) for r in data if r.get("WHO Region")=="Europe"]

# print(sum(recovered_patients))

#8 average recovered patient in europe region

average_recovered=sum(recovered_patients)/len(recovered_patients)

print(average_recovered)
