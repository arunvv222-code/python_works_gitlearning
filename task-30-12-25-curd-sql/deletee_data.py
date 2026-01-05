from mysql import connector

connection=connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="stationary_shop"
)

cursor=connection.cursor()

query="delete from products where id =%s"

data=(4,)

cursor.execute(query,data)
connection.commit()

cursor.close()
connection.close()

