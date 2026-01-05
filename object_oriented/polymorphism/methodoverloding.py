
"""
method overloading
"""

class calculator:
    def   add(sself,num1,num2):
        print(num1+num2)

    def add(self,num1,num2,num3):
        print(num1+num2+num3)

    def add(self,num1,num2,num3,num4):
        print(num1+num2+num3+num4)


cal_instance=calculator()

# cal_instance.add(100+200) (theese two methods canot be called because python now have 4 parameter)

# cal_instance.add(100+200,300)

cal_instance.add(100,200,300,400)