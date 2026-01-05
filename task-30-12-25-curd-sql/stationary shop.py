from mysql import connector

connection=connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="stationary_shop"
)

cursor=connection.cursor()

query=""" 

create table products(
        id int primary key auto_increment,
        name varchar(100) not null,
        price int not null,
        stock_quantity int not null

);
"""

cursor.execute(query)

print ("table created")