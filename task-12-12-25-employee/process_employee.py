
import csv

class Empoyee:
    data:list

    def __init__(self):
        file_path="task-12-12-25-employee\\employee_salary_dataset.csv"
        fr=open(file_path,"r")
        reader=csv.DictReader(fr)
        self.data=[row for row in reader]

    def length_data(self):
        print(len(self.data))

    def highest_salary(self):

        self.salary=[int(r.get("Monthly_Salary")) for r in self.data]

        self.max_salary=max(self.salary)

        self.highest_salry_emp=[r.get("Name") for r in self.data if int(r.get("Monthly_Salary"))== self.max_salary ]

        print(self.highest_salry_emp)

    def count_employee(self):
        # count of employee department wise

        self.dep_count={}

        for  r in self.data:

            self.dept=r.get("Department")

            if self.dept in self.dep_count:

                self.dep_count[self.dept]+=1
            else:
                self.dep_count[self.dept]=1

        print(self.dep_count)


    def phd_emp(self):

        # male emp with educationn level phd

        self.male_phd=[ r.get("Name") for r in self.data 
                       if r.get("Gender")=="Male" and r.get("Education_Level")=="PhD"]
        
        print(self.male_phd)
        

        


emp_instance1=Empoyee()

# emp_instance1.length_data()
# emp_instance1.highest_salary()
# emp_instance1.count_employee()
emp_instance1.phd_emp()


