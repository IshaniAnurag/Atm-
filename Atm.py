class Atm:
    def __init__(self,CardNumber,Pin):
        self.CardNumber=CardNumber
        self.Pin=Pi
    def CashWithdrawl(self,Amount):
        newAmount=50000-Amount
        print("your money has been withdrawed from the given account")
    def Balance(self,Balance):
        print("Your Balance is 50000")

def main():
    CardNumber=input("Please give your card number :")
    Pin=input("Enter your Pin")
    newUser=Atm(CardNumber,Pin)
    print("Choose your Activity")
    print("1.Balance Enquiry,2.Withdraw")
    activity=int(input("Select the acivity"))
    if(activity==1):
        newUser.Balance()
    elif(activity==2):
        amount=int(input("Enter the amount:"))
        newUser.CashWithdrawl(amount)
    else:
        print("Enter a valid number for the activity")

if __name__=="__main__":
    main()
    




            
