from  mysql import connector

connection = connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="tripwisedb"

)

cursor=connection.cursor()

query="delete  from user where id = %s"

data=(3,)
cursor.execute(query,data)
connection.commit()


print("data deleted")

cursor.close()
connection.close()


