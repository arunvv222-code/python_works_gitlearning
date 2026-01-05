treasure={
    "box1":"gold",
    "box2":"silver",
    "box3":"diamond",
    "box4":"platinum"
}

# print(treasure["box3"])

# if "box6" not in treasure:

#     treasure["box6"]="iron"
# print(treasure["box6"])


# itersting

# for k in treasure:  # key is the key dictionary only iterate keys

#     # print(k,treasure[k])0

#     print(k)

# using key()and value()

# for k in treasure.keys():
#     print("key=",k)

# for v in treasure.values():

#     print("values=",v)

# for k,v in treasure.items():

    # print(k,v)

print(treasure.get("box10"))

print(treasure.get("box10","empty set"))

treasure.pop("box2")

print(treasure)


