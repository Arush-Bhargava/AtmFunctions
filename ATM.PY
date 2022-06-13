import random

def atm():
    cardNumber = int(input("Enter your atm card number : "))
    pinNumber = int(input("Enter your pin card number : "))
atm()

def Balance_enquiry():
    rno = random.randint(10000,1000000)
    print("You currently have ₹"+str(rno) +"in your bank account")
Balance_enquiry()

def CashWithdrawl():
    Cash = input("Enter the amount you want to withdraw : ")
    print("you have successfully withdrawn ₹"+ Cash)
CashWithdrawl()