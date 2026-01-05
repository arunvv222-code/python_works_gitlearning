class Bank:
    acc_num=int
    name=str
    acc_type=str
    balance=int

    def create_account(self,acc_num,name,acc_type,balance):
        self.acc_num=acc_num
        self.name=name
        self.acc_type=acc_type
        self.balance=balance

        print(f"hai{self.name}your account with{self.acc_num}was created")

    def deposit(self,amount):
        self.balance+=amount
        print(f"your account number {self.acc_num} crdited with {amount} your available {self.balance}")

    def withdraw(self,amount):
        if amount<self.balance:
            self.balance-=amount
            print(f"your account {self.acc_num} credited with {amount} your avilable {self.balance}")
        else:
            print("transaction failes insufficient balance")
    def get_balance(self):
        print(f"hai {self.name} available balance {self.balance}")


account=Bank()
account.create_account(123,"arun","savings",1000)
account.deposit(100)
account.withdraw(30)
account.get_balance()
