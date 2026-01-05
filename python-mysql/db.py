from mysql import connector

connection=connector.connect(
        host='localhost',
        user="root",
        password="Password@123",
        database="pi_db"
)

print("connection success")