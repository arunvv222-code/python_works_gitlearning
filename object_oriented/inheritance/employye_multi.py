class employee:
    id:int
    department:str
    salary:int

    def __init__(self,id,department,salary):
        self.id=id
        self.department=department
        self.salary=salary

    def display(self):
        print(f"id: {self.id} deprtment {self.department} salary: {self.salary}")

class developer(employee):
    
    def __init__(self, id, department, salary,pg_lag,framework):
        super().__init__(id, department, salary)

        self.pg_lag=pg_lag
        self.framework=framework

    def display(self):
        super().display()
        print(self.pg_lag,self.framework)

devp_instance1=developer(123,"web devp",35000,"python","django")

devp_instance1.display()


        