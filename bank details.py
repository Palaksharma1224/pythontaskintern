class Bank:
    def __init__(self,name,accno,acc_type,balance):
        self.name=name
        self.accno=accno
        self.acc_type=acc_type
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print("balance",amount)

    def withdraw(self,amount):
        self.balance-=amount
        print("balance=",amount)

    def check_balance(self):
         return self.balance
        
a=Bank("HDFC",7637467,"saving",50000)
a.deposit(1000)
a.withdraw(2000)
a.check_balance()