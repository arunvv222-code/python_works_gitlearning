from mysql import connector

connection=connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="tripwisedb"
)

cursor=connection.cursor()

query="""
    insert into user(name,email,password) values(%s,%s,%s)

"""

data=[
    ("arun","arun@gmail.com","arun@123"),
    ("varun","varun@gmail.com","varun@123"),
    ("ardhra","ardhra@gmail.com","ardhra@123"),
    
    ("adithyan","adhithyan@gmail.com","adhithyan@123")


]


cursor.executemany(query,data)

connection.commit()

cursor.close()
connection.close()

print("value inserted")