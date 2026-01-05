import csv

class Toyota:

    def __init__(self):
        file_path="task-10-12-25-toyota\\toyota.csv"
        
        fr=open(file_path,"r",encoding='utf-8')
        
        reader=csv.DictReader(fr)
        self.data=[row for row in reader]

    def total_records(self):

        print(len(self.data))

    def firts_five_row(self):

        print(self.data[:5])

    def count_petrol_vehicle(self):

        self.petrol=[r.get("fuelType") for r in self.data if r.get("fuelType")=="Petrol"]

        print(len(self.petrol))

    def highest_price_model(self):

        self.price_toyota=[int(r.get("price")) for r in self.data]

        self.max_price=max(self.price_toyota)

        self.result=[r.get("year") for r in self.data if self.max_price== int(r.get("price"))]

        print(self.result)

    def highest_milage_model(self):

        self.milage=[int(r.get("mileage")) for r in self.data]

        self.max_milege=max(self.milage)

        self.hg_mil_model=[r.get("model") for r in self.data if int(r.get("mileage"))==self.max_milege]

        print(self.hg_mil_model)

    def highest_tax_vehicle(self):

        self.tax=[int(r.get("tax")) for r in self.data]

        self.max_tax=max(self.tax)

        self.result={r.get("model"): r.get("tax") for r in self.data if int(r.get("tax"))==self.max_tax}

        print(self.result)

    def price(self):

        self.price_data=[r.get("model") for r in self.data if 10000 <int(r.get("price"))<20000]

        print(self.price_data)

   

Toyota_instance=Toyota()

# Toyota_instance.total_records()

# Toyota_instance.firts_five_row()

# Toyota_instance.count_petrol_vehicle()

# Toyota_instance.highest_price_model()

# Toyota_instance.highest_milage_model()

# Toyota_instance.highest_tax_vehicle()

Toyota_instance.price()

