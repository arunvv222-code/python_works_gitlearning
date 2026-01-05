class course:
    course_name:str
    
    def __init__(self,course_name):

        self.course_name=course_name

    def display(self):
        print("course name",self.course_name)

class module(course):

    def __init__(self,course_name,module_name):
        super().__init__(course_name)

        self.module_name=module_name

    def display(self):
        super().display()

        print("module name ",self.module_name)

class lesson(module):

    def __init__(self, course_name, module_name,lesson_name):
        super().__init__(course_name, module_name)

        self.lesson_name=lesson_name

    def display(self):
        super().display()

        print("lesson name ",self.lesson_name)


lesson_instance=lesson("django","python","multi inheritance")

lesson_instance.display()