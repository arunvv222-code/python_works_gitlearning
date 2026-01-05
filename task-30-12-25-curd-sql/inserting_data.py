from mysql import connector

connection=connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="stationary_shop"
)

cursor=connection.cursor()

query="insert into products(name,price,stock_quantity)values(%s,%s,%s)"

data=[
    ("toot_paste",50,100),
    ("maggie",45,200),
    ("pencil",10,150),
    ("pen",7,500),
    ("bathing_soap",10,250)

]

cursor.executemany(query,data)

connection.commit()

print("query is inserted")

cursor.close()
connection.close()