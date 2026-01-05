import csv

class AiDataset:

    data:list

    def __init__(self):
        filepath="object_oriented\\ai_impact_dataset\\AI_Impact_on_Jobs_2030.csv"

        fr=open(filepath,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data=[row for row in reader]

    def total_records(self):

        print(len(self.data))
    def  display_first_record(self):
        print(self.data[0])


ai_inatance=AiDataset()

ai_inatance.total_records()

ai_inatance.display_first_record()



