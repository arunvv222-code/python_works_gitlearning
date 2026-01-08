from json import load

file_path="task1-8-1-26-oscar-jison\\oscar-best-picture-award-winners.json"

fr=open(file_path,"r",encoding="utf-8")

data=load(fr)

# print(len(data))

# print(data)

#Q1. Create a new list that contains only the movie titles from the dataset

movies_title=[r.get("name") for r in data]
# print(movies_title)

#Q2. Create a list that contains the movie title and 
# release year for each Oscar-winning film

result={r.get("name"):r.get("released_year") for r in data}
# print(result)

#Q3. Get all movies that were released before the year 2000.

movie_bf_2000=[r.get("name") for r in data if int(r.get("released_year"))< 2000]

# print(movie_bf_2000)

#Q4. Find all movies whose runtime is greater than 150 minutes.

# run_time=[r.get("name") for r in data if r.get("duration")>150]

# print(run_time)

#Q5.Create a list of movies where the director name starts with the letter “S”.

directors=[r.get("directors") for r in data]

# for d in directors:
#     for r in d:
#         if str(r).startswith("S"):
#             # print(r)


#Q6.Count the total number of Oscar-winning movies in the dataset.

# print("total number of oscar wining movie=",len(data))


#Q9.Find the earliest released movie in the dataset.

movie_year=[int(r.get("released_year")) for r in data ]

earliest_released=[r.get("name") for r in data if int(r.get("released_year"))==min(movie_year)]

# print(earliest_released)

#12. Find all movies that were released after 2015 and won the Oscar.

result1=[r.get("name") for r in data if int(r.get("released_year"))>2015]

print(result1)