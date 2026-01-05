class Mobile:
    title:str
    price:int
    brand:str
    features:str

    def __init__(self,title,price,brand,features):

        self.title=title
        self.price=price
        self.brand=brand
        self.features=features

    def display(self):
        print(f"title:{self.title} priice:{self.price} brand:{self.brand} feature:{self.features}")

i_phone=Mobile("iphone 15",59000,"apple","camera")

samsung=Mobile("s24",70000,"samsung","samsung ai")

i_phone.display()
samsung.display()
    