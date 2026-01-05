import csv

class HeartDisease:

    def __init__(self):
        
        file_path="task-15-12-25-heart_deasise\\Heart_Disease_Prediction.csv"
        fr=open(file_path,"r")
        reader=csv.DictReader(fr)
        self.data=[row for row in reader]

    def length_data(self):

        print(len(self.data))

    def count_heart_patient(self):
        self.patient_disease=[r.get("Age") for r in self.data if r.get("Heart Disease")=="Presence"]

        count=len(self.patient_disease)

        print(count)

    def patients_count_age(self):

        # patients with age above 50

        self.age=[r.get("Age") for r in self.data if r.get("Age")>"50"]

        print(len(self.age))

    def patients_avg_col(self):

        #Find the average cholesterol level for patients with heart disease.

        cholostrol=[int(r.get("Cholesterol")) for r in self.data if r.get("Heart Disease")=="Presence"]

        avg_chol=sum(cholostrol)/len(cholostrol)

        print(avg_chol)

    def male_female_rate(self):

        #Group patients by sex and calculate the heart disease rate.
        #(male_heart_disease / total_males) * 100

        patien_sex=[r.get("Sex") for r in self.data if r.get("Heart Disease")=="Presence"]

        total_patients=[r.get("Sex") for r in self.data]

        rate_male=(patien_sex.count("1")/total_patients.count("1"))*100

        rate_female=(patien_sex.count("0")/total_patients.count("0"))*100

        print("heart disease rate male=",rate_male)
        print("heart disease rate male=",rate_female)




heart_instance=HeartDisease()

# heart_instance.length_data()
# heart_instance.count_heart_patient()
# heart_instance.patients_count_age()
# heart_instance.patients_avg_col()
heart_instance.male_female_rate()