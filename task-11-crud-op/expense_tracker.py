
from mysql import connector


class ExpenseTracker:

    def __init__(self):
        
        try:
            self.connection=connector.connect(
            user="root",
            host="localhost",
            password="Password@123",
            database="expense_task"
            )

            self.cursor=self.connection.cursor()

            print("data base is connected")

        except Exception as e:
             print(e)

    def create_table(self):
        try:
            query="""
                create table expense(
                        id int primary key auto_increment,
                        title varchar(100) not null,
                        amount int not null,
                        category enum('food','travel','fuel','health','bills','other') default'other',
                        created_at datetime default current_timestamp
                        );
            """

            self.cursor.execute(query)
            self.connection.commit()

            print("table is created")
        except Exception as e:
            print(e)

    def insert_value(self,**kwargs):

        #title=bf,amount=40,category=food
        try:
            columns=""
            values=""
            for k,v in kwargs.items():
                columns+= k+ ","
                values+= "%s" + ","
            columns=columns.rstrip(",")
            values=values.rstrip(",")

            query=f"insert into expense({columns}) values({values})"

            data=[v for k,v in kwargs.items()]

            self.cursor.execute(query,data)
            self.connection.commit()

            print("data inserted")

        except Exception as e:
            print(e)

    def list_expense(self):

        try:
            query=f"select * from expense"
            self.cursor.execute(query)
            records=self.cursor.fetchall()
            for row in records:
                print(row)
        except Exception as e:
            print(e)

    def update_expense(self,id=None,**kwargs):
        try:
            place_holder=""

            for k,v in kwargs.items():
                place_holder+=k+"="+"%s"+","
            place_holder=place_holder.rstrip(",")

            query=f"update expense set {place_holder} where id={id}"

            data=[v for k,v in kwargs.items()]

            self.cursor.execute(query,data)
            self.connection.commit()
            print("table is updated")
        except Exception as e:
            print(e)

    def delete_data(self,id=None):
        query=f"delete from expense where id={id}"

        self.cursor.execute(query)
        self.connection.commit()

        print("query deleted")



expense_instance=ExpenseTracker()
# expense_instance.create_table()
# expense_instance.insert_value(title="fever",amount=1000,category="health")
expense_instance.list_expense()
# expense_instance.update_expense(id=2,title="ooty")
expense_instance.delete_data(id=4)



