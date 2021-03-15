class Cash_Details:
    def __init__(self):
        self.balance = 0
        print("Hello Customer")

    def deposit(self):
        amount = float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:", amount)
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if  self.balance >= amount:
            self.balance -= amount
            print("\n You have  Withdrawn:", amount)
        else:
            print("\n Insufficient balance ")

    def display(self):
            print("\n Net Available Balance=", self.balance)
            print("ACno : 101444555678 Name : Rinu Sebastian AcType : Savings" "Balance: ", self.balance)


s = Cash_Details()
s.deposit()
s.withdraw()
s.display()