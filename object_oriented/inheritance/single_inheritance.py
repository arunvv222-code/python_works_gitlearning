class person:
    name:str
    age:int
    gender:str
    def __init__(self,name,age,gender):

        self.name= name
        self.age= age
        self.gender= gender

    def display(self):

        print(f"name:{self.name} age:{self.age} gender:{self.gender}")

class student(person):

    def __init__(self, name, age, gender,rollnum,course):

        super().__init__(name,age,gender)

        self.rollnum=rollnum

        self.course=course

    def display(self):
        super().display()
        print(self.rollnum,self.course)
       
student_instance=student("arun",23,"male",1234,"django")

student_instance.display()
        