class ATM:
    def __init__(self):
        self.accounts={}
        self.transactions={}
    def create_account(self,userid,userpin,userbalance=0):
        self.userid=userid
        self.userpin=userpin
        self.userbalance=userbalance
        self.accounts[self.userid]=[self.userpin,self.userbalance]
        print("Your account has been created successfully!")
    def access_account(self,userid,userpin):
        self.userid=userid
        self.userpin=userpin
        for key,val in self.accounts.items():
            if self.userid==key:
                if self.userpin==val[0]:
                    return True
        return False
    def withdraw_amount(self,useramount):
        self.useramount=useramount
        if(self.useramount>self.accounts[self.userid][1]):
            print("No sufficient balance in your account!")
        else:
            self.accounts[self.userid][1]-=self.useramount
            self.transactions['Withdraw']=self.useramount
            print("Withdraw successfully completed!")
            print("Total Balance: ",self.accounts[self.userid][1])
    def deposit_amount(self,useramount):
        self.useramount=useramount
        self.accounts[self.userid][1]+=self.useramount
        self.transactions['deposit']=self.useramount   
        print("Amount deposited successfully!")   
        print("Total Balance: ",self.accounts[self.userid][1])
    def transaction(self):
        for key,val in self.transactions.items():
            print(key,":",val) 
    def transfer(self,target,useramount):
        self.target=target
        self.useramount=useramount
        for key in self.accounts.keys():
            if key==self.target:
                self.withdraw_amount(self.useramount)
                self.accounts[self.target][1]+=self.useramount
                self.transactions['transfer']=self.useramount
                print("Total Balance: ",self.accounts[self.userid][1])
                return True
        return False
                
user=ATM() 
while(True):
    print("\n......................................... ATM INTERFACE .................................................")
    print("1.Create Account")
    print("2.Access Account")
    print("3.Quit")
    print("..........................................................................................................\n")
    ch=int(input("Enter your choice:"))
    if(ch==1):
        print("Create your account")
        userid=int(input("Enter user id: "))
        userpin=int(input("Enter pin number: "))
        userbalance=int(input("Enter balance: "))
        user.create_account(userid,userpin,userbalance)
    elif(ch==2):
        print("Enter your details")
        userid=int(input("Enter user id: "))
        userpin=int(input("Enter pin number: "))
        res=user.access_account(userid,userpin)
        if(res):
            while(True):
                print("\n........ Options .........")
                print("1.Withdraw")
                print("2.Deposit")
                print("3.transaction")
                print("4.transfer")
                print("5.Quit")
                print("...........................\n")
                ch=int(input("Enter your choice"))
                if(ch==1):
                    useramount=int(input("Enter amount to be withdraw from your account: "))
                    user.withdraw_amount(useramount)
                elif(ch==2):
                    useramount=int(input("Enter amount to be deposit to your account: "))
                    user.deposit_amount(useramount)
                elif(ch==3):
                    user.transaction()
                elif(ch==4):
                    target=int(input("Enter transaction id: "))
                    useramount=int(input("Enter amount to be transfer: "))
                    result=user.transfer(target,useramount)
                    if(result):
                        print("Amount transferred successfully!")
                    else:
                        print("Transfer failed. Please try again!")
                elif(ch==5):
                    print("Thank you!")
                    break
        else:
            print("Create your account")
    elif(ch==3):
        print("Have a nice day. Thank you!")
        break