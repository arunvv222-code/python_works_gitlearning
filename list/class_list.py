language = ["c","c++","java"]

language.append("html")

print(language)

language.pop(1)

poped_value= language.pop(1)

print(language)

language.insert(3,"python")
print(language)

# language.remove("c++")

# print(language)

language.index("java")

pos = language.index("java")

print(pos)

language.count("c++")

freq=language.count("c++")

# print(freq)

language.sort()
# print(language)

language.sort(reverse=True)
# print(language)


language01=["java","python","html"]
language01.reverse()

# print(language01)


arun_fav_food=["biryani","putu","chore","mandhi"]

latha_fav_food=arun_fav_food.copy()

# print(latha_fav_food)

latha_fav_food[0]="chaya"

print("latha ",latha_fav_food)

print("arun ",arun_fav_food)



