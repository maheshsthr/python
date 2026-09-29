#Create a Bank class with two variables Name and Balance. Implement
#a constructor to initialize the variable. Also implement deposit and
#withdrawal using instance methods.

class Bank:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    def deposit(self,amount):
        if(amount>0):
            self.balance += amount
            print(f"Deposit Success. Balance : {self.balance}")
        else:
            print("Invalid Amount. Deposit Failed")

    def withdraw(self,amount):
        if(amount>0):
            if(amount<self.balance):
                self.balance -= amount
                print(f"Withdrawal Success. Balance : {self.balance}")
            else :
                print("Insufficient Balance")
        else:
            print("Invalid Amount. Withdrawal Failed")

holder1 = Bank("Holder1",50000)
holder2 = Bank("Holder2",60000)

holder1.withdraw(100000)


