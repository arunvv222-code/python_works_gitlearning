class Animal:

    def __init__(self,name):

        self.name=name
        

    def sound(self):

        print(self.name,"sound")

class Dog(Animal):
    
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print(self.name,"barking")

class Cat(Animal):

    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print(self.name,"meow")

dog_instance=Dog("dobber")

Cat_instance=Cat("percian cat")


dog_instance.sound()

Cat_instance.sound()