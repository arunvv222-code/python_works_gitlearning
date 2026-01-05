file_path="task 26-11-25\\pytho_movies_File.csv"

fr=open(file_path,"r")

import csv

reader=csv.DictReader(fr)

data=[r for r in reader]

header=reader.fieldnames
# print(header)

# print(data)

# print 5 rows 

count=0
for row in data:
    print(row)
    count+=1
    if count==5:
        break

# movie count

movie_count=len(data)
# print("movie conut=",movie_count)

rating_movies=[r.get("Audience score %") for r in data]

max_rating=[r.get("Film") for r in data if r.get("Audience score %")==max(rating_movies)]

# print(max_rating)

# year=int(input("enter a year"))

# for r in data:
#     if year==int(r.get("Year")):
#         print(r.get("Film"))
        
gener=input("enter gener ")

mov_gen={r.get("Film"):r.get("Genre").casefold() for r in data}

gener_movie=[k for k,v in mov_gen.items() if v==gener]

# print(gener_movie)










