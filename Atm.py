from types import new_class

class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin
    def balanceinquiry(self):
        print("Your Balance is ₹100")
    def cashwithdrawal(self,amount):
        new_amount = 100-amount
        print("You Withdrawed: "+str(amount)+" Your Balance is: "+str(new_amount))

def main():
    print("Hi! Welcome to Virtual-Automated teller machine(V-ATM) :)")
    name = input("Please Enter Your Name--")
    print("Hello "+name)
    cno = input("Please Enter Your CardNumber--")
    pw = input("Please Enter Your Pin--")
    nu = Atm(cno,pw)

    print("What do you perfer "+name+"?")
    print("1. Balance Inquiry")
    print("2. Cash Withdrawal")
    pre = int(input("Enter Your Preference ( 1 or 2? )--"))

    if (pre == 1):
        nu.balanceinquiry()
    elif (pre == 2):
        amount = int(input("Enter the amount--"))
        nu.cashwithdrawal(amount) 
    else:
        print("Enter a valid preference number--")

if __name__ =="__main__":
    main()