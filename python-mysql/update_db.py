
# update data of table


from mysql import connector

connection=connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="tripwisedb"
)

cursor=connection.cursor()

query="update user set name=%s , password=%s where id=%s "

data=("varun v v","varunvv@gmail.com",4)

cursor.execute(query,data)

connection.commit()

print("record update")

cursor.close()
connection.close()



