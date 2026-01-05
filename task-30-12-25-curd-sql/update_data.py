from mysql import connector

connection=connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="stationary_shop"
)

cursor=connection.cursor()

query="update products set name=%s where id =%s"

data=("yippe",2)

cursor.execute(query,data)

connection.commit()

print("data updated")

cursor.close()
connection.close()