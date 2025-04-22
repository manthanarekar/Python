# Abstraction : It is way of hiding implementation details and showing only functionality to user. i.e internal process will not br reaveal to user

# There are two ways of representing abstraction
# 1) Via localmethod
# 2) Via ABC class -> abstractmethod


class ATM:
    def __init__(self, debitamount):
        self.balance = 1000
        self.debitamount = debitamount

    def getabalance(self):
        minbalance = 1000

        if self.balance - self.debitamount >= minbalance:
            self.balance = self.balance - self.debitamount
            print("Amount debited")
            print(f"Current balance : {self.balance}")
        else:
            print("! Balance insifficient")
            print(f"Current balance : {self.balance}")


amount = float(input("Enter Debit ampunt : "))
a = ATM(amount)
a.getabalance()
