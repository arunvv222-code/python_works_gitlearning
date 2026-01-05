class Car:
    name:str
    brand:str
    price:int
    color:str

    def set_car(self,name,brand,price,color):
        self.name=name
        self.brand=brand
        self.price=price
        self.color=color

    def display(self):
        print(self.name)
        print(self.brand)
        print(self.price)
        print(self.color)

car_instance1=Car()

car_instance2=Car()

car_instance1.set_car("swift","maruthi",800000,"black")
car_instance2.set_car("porsche 911","porsche",30000000,"red")

car_instance1.display()
car_instance2.display()
