# set_a= {100,200,300,400}
# set_b= {10,20,30,40,300,400}

# print(set_a.union(set_b))
# print(set_a.intersection(set_b))
# print(set_a.difference(set_b))

set_a= {100,200,300,400}
set_b= {300,400}

# print(set_a.issuperset(set_b))
# print(set_b.issuperset(set_a))


all_user={"sachin","dravid","laxman","gangully","sreenath","zaheer","dhoni","yuvi","kaif"}

sachin_friends={"dravid","laxman","ganguly"}
dhoni_friends={"dravid","laxman","yuvi","kaif"}

common_friends=sachin_friends.intersection(dhoni_friends)
print(common_friends)

# suggestion=all_user.difference(sachin_friends)

# suggestion.remove("sachin")

# print(suggestion)


set_a1={100,200,300,400,10,20}
set_b1={10,20,100,200,500,600,700}

print(set_a1.symmetric_difference(set_b1))


set_food={"tea","coffe","dosa"}

set_food.add("friderice")

print(set_food)

set_food.remove("tea")

print(set_food)