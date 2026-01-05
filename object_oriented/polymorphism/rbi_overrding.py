class Rbi:
    def gold_loan_rate(self):

        print("gold loan rate",8.5)

    def home_loan_rate(self):

        print("home loan rate",9.2)

    def car_loan_rate(self):

        print("car loan rate",8.5)

class HDFC(Rbi):

    def  gold_loan_rate(self):
        print("gold loan rate",9.5)

    def home_loan_rate(self):
        print("home loan rate ",10)

    def car_loan_rate(self):
        print("car loan rate",9.7)

bank_instance=HDFC()

bank_instance.gold_loan_rate()

bank_instance.home_loan_rate()

bank_instance.car_loan_rate()

