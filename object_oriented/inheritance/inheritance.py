"""
Docstring for object_oriented.inheritance

mechnism of child class accessing properties and attributes of parent class

syntax:
class parent:
    def ml(seld):
        print("parent class methods")
class child(parent):
    def m2(self):
        print("child class m2 method")

child_instance=child()

child_instance.m2()

child_instance.m1()

"""
# single inheritance

class parent:

    def vehicle(self):

        print("passion pro")

class child(parent):

    def mobile(self):

        print("iphome 15")
 
child_instance=child()

child_instance.mobile()

child_instance.vehicle()