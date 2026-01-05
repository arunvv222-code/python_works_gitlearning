from mysql import connector

connection=connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="tripwisedb"

)

cursor = connection.cursor()

query="""

create table user(
    id int primary key auto_increment,
    name varchar(100) not null,
    email varchar(100) not null,
    password varchar(100) not null

);

"""

cursor.execute(query)

print("table created")