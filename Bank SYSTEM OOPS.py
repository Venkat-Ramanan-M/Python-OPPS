class User:
    count=0
    def __init__(self,name,age,aadhar,phone,address,accno,atmpin):
        self._name = name
        self._age = age
        self._aadhar = aadhar
        self._phone = phone
        self._address = address
        self._accno=accno
        self._atmpin=atmpin
        User.count+=1
    def displayDetails(self):
        print("\nName           : ",self._name)
        print("Age            : ", self._age)
        print("Aadhar         : ",self._aadhar)
        print("Phone          : ",self._phone)
        print("City           : ",self._address)
        print("Account Number : ", self._accno)
        print("ATM PIN        : ", self._atmpin)
    def displayBlance(self):
        print("\nName                   : ",self._name)
        print("Account Number         : ", self._accno)

    def phoneChange(self,newno):
        self._phone=newno
        print("\nPhone Number changed successfully!!!")
    def addressChange(self,newadd):
        self._address=newadd
        print("\nAddress changed successfully!!!")
    def pinChange(self,newpin):
        self._atmpin=newpin
        print("\nATM PIN changed successfully!!!\t***KEEP IT SAFE***")
    def accountCreation(self):
        print("\nAccount Number         : ", self._accno)
        print("Temporary Pin          : ",self._atmpin)
class Bank(User):
    def __init__(self,name,age,aadhar,phone,address,accno,atmpin):
        super().__init__(name,age,aadhar,phone,address,accno,atmpin)
        self.balance=0

    def deposit(self,amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("\nAccount Balance has been Updated")
        print("\nBalance: ",self.balance)

    def withdraw(self,amount):
        self.amount = amount
        if(self.amount > self.balance):
             print("\nBalance Insufficient!")
             print("\nYour Available Balance: ",self.balance)
        else:
            self.balance = self.balance - self.amount
            print("\nBalance after Withdrawl: ",self.balance)

    def viewBalance(self):
        self.displayBlance()
        print("Your Available Balance : ",self.balance)

msg="""
    Enter 1 >for> Account Creation and Corrections
    Enter 2 >for> ATM services
    Enter 3 >>to> Quit Banking Service
"""
msgg="""
    Enter 1 >for> Account Creation
    Enter 2 >for> Corrections
    Enter 3 >>to> GO BACK!
"""
msg1="""
    Enter 1 >for> Display Details
    Enter 2 >for> Change Phone Number
    Enter 3 >for> Change in Address
    Enter 4 >>to> GO BACK!
"""
msg2="""
    Enter 1 >for> Balance Detail
    Enter 2 >for> Deposit
    Enter 3 >for> Withdraw
    Enter 4 >for> ATM PIN Change
    Enter 5 >>to> GO BACK!
"""
while(True):
    print(msg)
    count=1
    ch=int(input("\nEnter your choice: "))
    if(ch==1):
        while(True):
            print("\nWELCOME TO OUR BANK!")
            print(msgg)
            chh=int(input("\nEnter Your Choice: "))
            if(chh==1):
                name=input("\nEnter your Name: ")
                age = input("Enter your Age: ")
                aadhaar = input("Enter your Aadhaar Number: ")
                phone = input("Enter your Phone Number: ")
                address = input("Enter your Address: ")
                accno = 35266240000001
                atmpin = 5555
                user1 = Bank(name,age,aadhaar,phone,address,accno,atmpin)
                accno += 1
                print("\nYOUR ACCOUNT HAS BEEN CREATED SUCCESFULLY!")
                user1.accountCreation()

            elif(chh==2):
                while(True):
                    print(msg1)
                    ch1=int(input("\nEnter Your Choice: "))
                    if(ch1==1):
                        user1.displayDetails()
                    elif(ch1==2):
                        phone1=input("\nEnter New Phone Number: ")
                        user1.phoneChange(phone1)
                    elif(ch1==3):
                        address1=input("\nEnter New Address: ")
                        user1.addressChange(address1)
                    elif(ch1==4):
                        break
                    else:
                        print("\nInvalid Entry!")
            elif(chh==3):
                break
            else:
                print("\nInvalid Entry!")
    elif(ch==2):
        while(True):
            pincheck=int(input("\nEnter 4 Digit PIN: "))
            if(pincheck==user1._atmpin):
                print(msg2)
                ch2=int(input("\nEnter Your Choice: "))
                if(ch2==1):
                    user1.viewBalance()
                elif(ch2==2):
                    deposit= int(input("\nEnter the Amount to be Deposited: "))
                    user1.deposit(deposit)
                elif(ch2==3):
                    wdaamt= int(input("\nEnter the Amount to be Withdrawn: "))
                    user1.withdraw(wdaamt)
                elif(ch2==4):
                    oldpin=int(input("\nEnter OLD PIN: "))
                    if(oldpin==user1._atmpin):
                        atm = input("\nEnter New 4 Digit ATM PIN: ")
                        atm1 = input("\nRenter New 4 Digit ATM PIN: ")
                        if(atm==atm1):
                            user1.pinChange(atm1)
                            break
                        else:
                            print("\nWrong Entries! Try After Sometime!")
                            break
                    else:
                        print("\nYou have Entered Wrong Pin! Try After Sometime")
                        break
                elif(ch2==5):
                    break
                else:
                    print("\nInvalid Entry!")
            else:
                print("\nWRONG PIN! Try After Sometime!")
                break
    elif(ch==3):
        print("\nTHANKS FOR USING OUR BANK!")
        quit()
    else:
        print("\nInvalid Entry!")
