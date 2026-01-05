file_path="task-28-11-25-spotify\\spotify_data clean.csv"

fr=open(file_path,"r",encoding="utf-8")

import csv

reader=csv.DictReader(fr)

data=[row for row in reader]

# print(len(data))

fst_five=[r for r in data][:5]

# print(fst_five)

artist_name={r.get("artist_name") for r in data }

# print(artist_name)

"""
Count explicit songs
Find how many tracks have explicit = True.
"""

excplicit_track=[r.get("track_name") for r in data if r.get("explicit")== "TRUE"]

# print(len(excplicit_track))

"""
Print track names with popularity more than 50
Display all track names where track_popularity > 50.
"""

popularity=[r.get("track_name") for r in data if float(r.get("track_popularity")) > 50]

# print(popularity)

"""
Write a program to find the track with the highest popularity.
"""
# print(max(popularity))

"""
Calculate and print the average value of track_popularity.
"""
sum_popularity=0
for r in data:
    if float(r.get("track_popularity")):
        sum_popularity+=float(r.get("track_popularity"))

all_popularity=[r.get("track_popularity") for r in data]

average_popularity=sum_popularity/len(all_popularity)

print("avg popularity=",average_popularity)

"""
Top 5 most followed artists
Find the top 5 artists with the highest artist_followers
"""












