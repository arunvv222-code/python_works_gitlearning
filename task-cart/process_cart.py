file_path="task-cart\\cart_items_100.csv"

fr=open(file_path,"r")

import csv

reader=csv.DictReader(fr)

data=[row for row in reader]

order_summary={}

for r in data:
    title=r.get("title")
    quantity=int(r.get("quantity",0))

    if title in order_summary:
        order_summary[title]+=quantity
    else:
        order_summary[title]=quantity

# print(order_summary)

max_order=[k for k,v in order_summary.items() if v==max(order_summary.values())]

# print(max_order)

min_order=[k for k,v in order_summary.items() if v==min(order_summary.values())]

# print(min_order)

for u in data:
    user=u.get("user")

max_user=[user for k,v in order_summary.items() if v==max(order_summary.values())]

print(max_user)