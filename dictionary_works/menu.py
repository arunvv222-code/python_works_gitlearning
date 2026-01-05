menu_items={
    "mandhi":200,
    "biriyani":150,
    "meals":70,
    "noodles":100,
    "mutton fry":500,
    "alpham":150
}

# for k in menu_items.keys():
#     print(k)

# for k,v in menu_items.items():
#     print(k,v)
for k,v in menu_items.items():
    if v< 100:
        print(k)

item_price=menu_items.get("mandhi",0)
print(item_price)

# chec the item exisst if exist update it 



if "mandhi" in menu_items:
    menu_items["mandhi"]+=15
    

print(menu_items)