class vehicle:
    
    def __init__(self,brand,title):
        
        self.brand=brand
        self.title=title

    def move(self):

        print(self.title,"is moving")

class Car(vehicle):
    
    def __init__(self, brand, title):
        super().__init__(brand, title)

class ship(vehicle):
    def __init__(self, brand, title):
        super().__init__(brand, title)

    def move(self):
        print(self.title,"is sailing")


car_instance=Car("totyota","LC")

ship_instance=ship("anglo eastern","the gaint")


car_instance.move()

ship_instance.move()

        