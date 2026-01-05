class Person:
    name:str
    age:int
    gender:str

    def __init__(self,name,age,gender):

        self.name=name

        self.age=age

        self.gender=gender
    
    @property
    def get_age(self):

        print(self.name)
    @property
    def get_gender(self):
        print(self.gender)



person_instance=Person("arun",22,"male")
        
person_instance.get_age

person_instance.get_gender