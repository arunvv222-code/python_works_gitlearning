class grandparents:
    def properties(self):

        print("50 cenr land 1 huge vintage home")

class parents(grandparents):

    def vehicles(self):

        print("swift car")

class child(parents):

    def gadget(self):

        print("iphone, ipad")

child_instance=child()

child_instance.properties()

child_instance.gadget()

child_instance.vehicles()
