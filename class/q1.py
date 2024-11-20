"""
3. Write a Python class BankAccount with attributes like account_number, balance, date_of_opening and
customer_name, and methods like deposit, withdraw, and check_balance.
"""
print("""
------------------------------------
        1.Bank Account
        2.deposit
        3. withdraw
        4.check_balance
        5.exit
------------------------------------     
""")
class BankAccount:
    def __init__(self,account,balance,date,name):
        self.account_number=account
        self.balance=balance
        self.date_of_opening=date
        self.customer_name=name
    def bank_account(self):
        print("Account Number =",self.account_number)
        print("Minimum Balance =",self.balance)
        print("Account opening Details =",self.date_of_opening)
        print("Cumstomer Name =",self.customer_name)
    def deposit(self):
        d=float(input("enter the Rs how many u want to deposit:"))
        self.Total_Rs=self.balance+d

    def withdraw(self):
        if self.balance>0:
            w=int(input("enter the RS to you want to withdraw:"))
            if w<self.Total_Rs:
                self.Total_Rs=self.Total_Rs-w
            else:
                print("your balance is less so you can't withdraw")
    def check_balance(self):
        print('Total RS:',self.Total_Rs)
bank=BankAccount(76890989006,100,"12.10.2000","Rahul Kumar")
while True:
    ch=input("enter your choice:")
    print("---------------------------------")
    match(ch):
        case '1':
            bank.bank_account()
        case '2':
            bank.deposit()
        case '3':
            bank.withdraw()
        case '4':
            bank.check_balance()
        case '5':
            break

