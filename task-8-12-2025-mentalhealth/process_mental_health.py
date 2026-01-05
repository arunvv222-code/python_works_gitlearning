file_path="task-8-12-2025-mentalhealth\\mental_health_social_media_dataset.csv"

fr=open(file_path,"r")

import csv

reader=csv.DictReader(fr)

data=[row for row in reader]

# print(len(data))

# which person have highest screen time

screen_time=[int(r.get("daily_screen_time_min")) for r in data ]

highest_st=max(screen_time)

p_highest_st=[r.get("person_name") for r in data if int(r.get("daily_screen_time_min",0)or 0)==highest_st]

# print(p_highest_st)

# number of males use instagram

inst_gender=[r.get("gender") for r in data if r.get("platform")=="Instagram"]

count_male=inst_gender.count("Male")

# print("no:of male use insta",count_male)

# number of feales use Snapchat

snap_gender=[r.get("gender") for r in data if r.get("platform")=="Snapchat"]

count_female=snap_gender.count("Female")

# print("no:of feamale use snapchat",count_female)

# average social media time for males

male_sm_time=[int(r.get("social_media_time_min")) for r in data if r.get("gender")=="Male"]

avg_sm_time_male=sum(male_sm_time)/len(male_sm_time)

# print(avg_sm_time_male)

# print the person name with highest sleep hour

sleep_hour=[float(r.get("sleep_hours")) for r in data]

max_sleephour=max(sleep_hour)

p_highest_slh=[r.get("person_name") for r in data if float(r.get("sleep_hours",0)or 0)==max_sleephour]

# print("person with highest st:=",p_highest_slh)

# no.of stressed people below age 25

stresed_people=[r.get("mental_state") for r in data if int(r.get("age"))<=50]

count_stressed=stresed_people.count("Stressed")
count_Healthy=stresed_people.count("Healthy")

# print("no of stressed ",count_stressed)
print("no of healthy ",count_Healthy)