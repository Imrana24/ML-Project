import datetime
def welcome_user():
    x=datetime.datetime.now()
    if x.hour<12:
        print("Good morning and have a nice day")
    elif x.hour==12:
        print("Good afternoon")
    elif x.hour>12 and x.hour<=20:
        print("Good evening")
    else:
        print("Oh,it's late")
welcome_user()
def greetings_user(): 
    print("Hello!,I am bot. I am here to show your bank balance")
greetings_user()
str=input("Enter your name:")
print("Hello:",str)
str1=int(input("Enter your Bank Account Number:"))
print("Bank Account Number:",str1)
class Bank_Account: 
    def __init__(self): 
        self.balance=0
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")
  
    def deposit(self): 
        amount=float(input("Enter amount to be Deposited: ")) 
        self.balance += amount 
        print("\n Amount Deposited:",amount) 
  
    def withdraw(self): 
        amount = float(input("Enter amount to be Withdrawn: ")) 
        if self.balance>=amount: 
            self.balance-=amount 
            print("\n You Withdrew:", amount) 
        else: 
            print("\n Insufficient balance  ") 
  
    def display(self): 
        print("\n Net Available Balance=",self.balance) 
  

s = Bank_Account() 
   
 
s.deposit() 
s.withdraw() 
s.display() 