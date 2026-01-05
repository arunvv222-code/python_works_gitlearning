
from mysql import connector

class product:

    def __init__(self):

        try:
            self.connection=connector.connect(

                user="root",
                host="localhost",
                password="Password@123",
                database="stationary_shop"
            )

            self.cursor=self.connection.cursor()

            print("db is connected")
        
        except Exception as e:
            print(e)

    def add_product(self,**kwargs):

        try:
            column=""
            value=""
            for k,v in kwargs.items():
                column+=k + ","
                value+="%s" + ","
            column=column.rstrip(",")
            value=value.rstrip(",")

            query=f"insert into products ({column}) values ({value})"
            
            data=[v for k,v in kwargs.items()]

            self.cursor.execute(query,data)
            self.connection.commit()

            print("produtcs added")
        except Exception as e:
            print(e)

    def list_product(self):
        try:
            query="select * from products"
            self.cursor.execute(query)
            records=self.cursor.fetchall()
            for row in records:
                print(row)
        except Exception as e:
            print(e)

    def retrive_product(self,id=None):
        try:
            qeury="select * from products where id=%s"
            data=(id,)
            self.cursor.execute(qeury,data)
            records=self.cursor.fetchone()
            print(records)
        except Exception as e:
            print(e)

    def delete_product(self,id=None):
        try:
            query="delete from products where id=%s"
            data=(id,)
            self.cursor.execute(query,data)
            self.connection.commit()
            print(" record is deleted")
        except Exception as e:
            print(e)

    def update_product(self,id,**kwargs):
            try:
                place_holder=""
                for k,v in kwargs.items():
                    place_holder+=k+"="+"%s"+","
                place_holder=place_holder.rstrip(",")
                query=f"update products set {place_holder} where id={id}"
                data=[v for k,v in kwargs.items()]

                self.cursor.execute(query,data)
                self.connection.commit()
                print("table updated")
            except Exception as e:
                print(e)


product_instance=product()
# product_instance.add_product(name="book",price=30,stock_quantity=120)
product_instance.list_product()
# product_instance.retrive_product(id=3)
# product_instance.delete_product(id=4)
product_instance.update_product(5,price=20,stock_quantity=200)
product_instance.list_product()