
# fetching one data from the table


from  mysql import connector

connection = connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="tripwisedb"

)

cursor=connection.cursor()

query=" select * from user where id= %s "

data=(3,)

cursor.execute(query,data)

records=cursor.fetchone()

print(records)