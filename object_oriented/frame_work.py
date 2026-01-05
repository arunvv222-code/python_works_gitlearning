class Framework:
    name:str
    language:str
    architecture:str

    def set_framework(self,name,language,arct):
        self.name=name
        self.language=language
        self.architecture=arct
    def display(self):
        print(self.name,self.language,self.architecture)

django= Framework()

asp=Framework()

django.set_framework("django","python","mvt")
asp.set_framework("asp","c#","mvc")

django.display()
asp.display()
