class account:
    
    def __init__(self, filename):
        self.newFile = filename
        with open(self.newFile, 'r') as file: 
            self.balance = int(file.read())
            #print(self.balance)

    def withdraw(self, amt):
        self.balance = self.balance - amt
        print(f"Amount withdrawn is Rs. {amt} and current balance is Rs. {self.balance}")
    
    def deposit(self, amt):
        self.balance = self.balance + amt
        print(f"Amount deposited is Rs. {amt} and current balance is Rs. {self.balance}")


    def alerts(self):
        if (self.balance < 200):
            print(f"Balance is low. Current balance is: {self.balance}")

    def commit(self):
        with open(self.newFile, 'w') as file:
            file.write(str(self.balance))


