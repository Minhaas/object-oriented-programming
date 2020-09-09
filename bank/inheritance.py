from bank import account 

#Demonstration of inheritance - Account is parent class and checking is child class

class checking(account):
    #Inherited class can also have their own instance variable, in this case, it is fee
    def __init__(self, filename, fee):
        account.__init__(self, filename)
        self.transFee = fee

    def transfer(self, amount):
        self.balance = self.balance - amount - self.transFee
        print(f"Amount transferred is Rs. {amount} and current balance is Rs. {self.balance}")

    
checkingAcc = checking("balance.txt",10)
checkingAcc.withdraw(50)
checkingAcc.deposit(20)
checkingAcc.transfer(100)
checkingAcc.commit()
checkingAcc.alerts()