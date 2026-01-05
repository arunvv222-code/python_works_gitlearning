from copy import deepcopy

# we need copy of ineer and outer of a object use deep copy
# used in nested list etc...

arun_fav_food=[
    ["dosa","tea"],
    ["meals","lime juice"],
    ["chapathy","lime tea"],
]

res_fav_food=deepcopy(arun_fav_food)

res_fav_food[0][0]="idily"


print("arun",arun_fav_food)
print("resvin",res_fav_food)