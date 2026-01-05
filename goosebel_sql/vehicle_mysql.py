
from mysql import connector


class vehicle:
    
    def __init__(self):
        try:
            self.connection=connector.connect(
                host="localhost",
                user="root",
                password="Password@123",
                database="gosell_db"
            )

            self.cursor=self.connection.cursor()

            print("db is connected")

        except Exception as e:
            print(e)

    
    def add_vehicle(self,**kwargs):
            
        try:    

            columns=""
            values=""
            for k,v in kwargs.items():
                columns+=k + ","
                values+="%s" + ","
            columns=columns.rstrip(",")
            values=values.rstrip(",")

            query=f" insert into vehicle ({columns}) values ({values}) "

            data=[v for k,v in kwargs.items()]

            self.cursor.execute(query,data)
            self.connection.commit()

            print("values is inserted")

        except Exception as e:
         print(e)

    
    def list_vehicle(self):
       
       try:
            query=" select * from vehicle"
            self.cursor.execute(query)
            records=self.cursor.fetchall()
            for row in records:
                print(row)
       except Exception as e:
           print(e)

    def  retrive_vehicle(self,id=None):
        try:
            query="select * from vehicle where id=%s"
            data=(id,)
            self.cursor.execute(query,data)
            records=self.cursor.fetchone() 
            print(records)   
        except Exception as e:
            print(e)

    def delete_vehicle(self,id=None):

        try:
            query="delete from vehicle where id=%s"
            data=(id,)
            self.cursor.execute(query,data)
            self.connection.commit()

            print("record deleted.....")
        except Exception as e:
            print(e)
    
    def  update_vehicle(self,id,**kwargs):
        place_holder=""
        for k,v in kwargs.items():
            place_holder+=k + "="+"%s"+","
        place_holder=place_holder.rstrip(",")
        
        query=f"update vehicle set {place_holder} where id = {id}"

        data=[v for k,v in kwargs.items()]

        self.cursor.execute(query,data)
        self.connection.commit()

        print("updated the query.....")
        

vehicle_instance=vehicle()
# vehicle_instance.add_vehicle(name="passion pro",price=23000,year=2022,fuel_type="petrol",comments="good",running_km=20000,owner_type="single",owner="adarsh",location="thrissur")
# vehicle_instance.list_vehicle()
# vehicle_instance.retrive_vehicle(id=4)
# vehicle_instance.delete_vehicle(id=5)
# vehicle_instance.list_vehicle()
vehicle_instance.retrive_vehicle(id=4)
vehicle_instance.update_vehicle(4,price=34000)
vehicle_instance.retrive_vehicle(id=4)
