import datetime

import os

def userlogin():
    print("\t***************************")
    print("\tBANKING SERVICE APPLICATION")
    print("\t***************************")
    userid = str(input("Please enter your user ID: "))
    userpass = str(input("Please enter your password: "))
    with open("userpass.txt","r") as fh:
        foundrec = "notfound"
        for recline in fh:
              reclist = recline.strip().split(":")
              if reclist[0] == userid and reclist[1] == userpass:
                    foundrec = reclist
                    break
        if foundrec == "notfound":
              print("Login not successful...!!!")
        else:
            print("Login Successful...")
    return foundrec

def genid(perm):
    with open("id.txt","r") as idfh:
        rec = idfh.readline()
        reclist = rec.strip().split(":")
        if perm == "staff":
            pref = "STF"
            oldid = reclist[0][3:]
        elif perm == "customer":
            pref = "CTM"
            oldid = reclist[1][3:]
    nextid = int(oldid) + 1
    if len(str(nextid)) == 1:
        newid = "0000"+str(nextid)
    elif len(str(nextid)) == 2:
        newid = "000"+str(nextid)
    elif len(str(nextid)) == 3:
        newid = "00"+str(nextid)
    elif len(str(nextid)) == 4:
        newid = "0"+str(nextid)
    elif len(str(nextid)) == 5:
        newid = str(nextid)
    newid = pref+newid
    if perm == "staff":
        reclist[0] = newid
    else:
        reclist[1] = newid
    rec = ":".join(reclist)
    with open("id.txt","w") as fh:
        fh.write(rec)
    return newid

def addstaff():
    userid = genid("staff")
    userpass = userid
    print("User ID :",userid)
    print("User Password:",userpass)
    usrname = input("Please enter your name : ")
    age = int(input("Please enter your age : "))
    phone_number = (str(input("Please enter your phone number [082122944783: 12 digits] : ")))
    while len(phone_number) < 12:
        print("The numbers you input either exceeded the limit or below 12!...")
        phone_number = (str(input("Please enter your phone number [082122944783: 12 digits] : ")))
    else:
        pass
    dateofbirth = datetime.datetime.strptime(input("Please enter your date of birth [Year-Month-Day: 2021-09-18] : "), "%Y-%m-%d")
    residential_address = input("Please enter your residential address : ")
    occupation = "******"
    accmodel = "Staff"
    amount = "******"
    acctype = "2"
    with open("userpass.txt","a") as fh:
        rec = userid+":"+userpass+":"+usrname+":"+acctype+":"+accmodel+":"+amount+":"+str(phone_number)+":"+str(dateofbirth.date())+":"+residential_address+":"+str(age)+":"+occupation+"\n"
        fh.write(rec)

def addcustomer(logdetails):
    userid = genid("customer")
    userpass = userid
    print("Customer ID :",userid)
    print("Customer Password:",userpass)
    usrname = input("Please enter your name : ")
    age = int(input("Please enter your age : "))
    phone_number = (str(input("Please enter your phone number [082122944783: 12 digits] : ")))
    while len(phone_number) < 12:
        print("The numbers you input either exceeded the limit or below 12!...")
        phone_number = (str(input("Please enter your phone number [082122944783: 12 digits] : ")))
    else:
        pass
    dateofbirth = datetime.datetime.strptime(input("Please enter your date of birth [Year-Month-Day] : "), "%Y-%m-%d")
    residential_address = input("Please enter your residential address : ")
    occupation = input("Please enter your occupation : ")
    amount = 0
    acctype = "3"
    accmodel = input("Please enter you account model [Savings/Current] : ")
    if accmodel == "Savings": 
        amount = int(input("Please enter your initial amount with the minimum of RM 100 : "))
        while amount <= 100:
            print("Invalid amount")
            amount = int(input("Please enter your initial amount with the minimum of RM 100 : "))
        else:
            print("Successful Customer ID Registration!")
    elif accmodel == "Current":
        amount = int(input("Please enter your initial amount with the minimum of RM 500 : "))
        while amount <= 500:
            print("Invalid amount")
            amount = int(input("Please enter your initial amount with the minimum of RM 500 : "))
        else:
            print("Successful Customer ID Registration!")
    else:
        print("You did not choose neither!...")
        return
    with open("userpass.txt","a") as fh:
        rec = userid+":"+userpass+":"+usrname+":"+acctype+":"+accmodel+":"+str(amount)+":"+str(phone_number)+":"+str(dateofbirth.date())+":"+residential_address+":"+str(age)+":"+occupation+"\n"
        fh.write(rec)

def dispalluser():
    with open("userpass.txt","r") as fh:
        print("="*190)
        print("User ID".center(10)+"|"+"User Password".center(14)+"|"+"User Name".center(15)+"|"+"Account Type".center(14)+"|"+"Account Model".center(15)+"|"+"Account Balance".center(17)+"|"+"Phone Number".center(15)+"|"+"Date of Birth".center(16)+"|"+"Residential Address".center(50)+"|"+"Age".center(5)+"|"+"Occupation".center(14)+"|")
        print("="*190)
        for rec in fh:
              reclist = rec.strip().split(":")
              print(reclist[0].ljust(10)+"|"+reclist[1].ljust(14)+"|"+reclist[2].ljust(15)+"|"+reclist[3].ljust(14)+"|"+reclist[4].ljust(15)+"|"+reclist[5].ljust(17)+"|"+reclist[6].ljust(15)+"|"+reclist[7].ljust(16)+"|"+reclist[8].ljust(50)+"|"+reclist[9].ljust(5)+"|"+reclist[10].ljust(14))
    print("\n\n\n")

def changepass(logdetails):
    allrec = []
    with open ("userpass.txt","r") as fh:
        for rec in fh:
            reclist = rec.strip().split(":")
            allrec.append(reclist)
    newpass = input("Please input your new password : ")
    ind = -1
    nor = len(allrec)
    for cnt in range (0,nor):
        if logdetails [0] == allrec[cnt][0]:
            ind = cnt
            break

    allrec[ind][1] = newpass
    with open("userpass.txt.","w") as fh:
        nor = len(allrec)
        for cnt in range(0,nor):
            rec = ":".join(allrec[cnt])+"\n"
            fh.write(rec)

def modifydetails():
    allrec = []
    with open ("userpass.txt","r") as fh:
        for rec in fh:
            reclist = rec.strip().split(":")
            allrec.append(reclist)        
    accountselect = input("Please enter the account you want to modify [Q if want to return to menu] : ")
    if accountselect == "Q":
        print("You have return to the menu!"+"\n")
        return
        
    ina = -1
    nor = len(allrec)
    for cnt in range (0,nor):
            if accountselect == allrec[cnt][0]:
                ina = cnt
                break
    print("\n\t1. User Password")
    print("\t2. Account Model")
    print("\t3. Phone Number")
    print("\t4. Date of Birth")        
    print("\t5. Residential Address")
    print("\t6. Age")
    print("\t7. Occupation")
    detailsselect = input("Which details do you want to modify : ")
    ind = -1
    if detailsselect == "1":
        ind = 1
    elif detailsselect == "2":
        ind = 4
    elif detailsselect == "3":
        ind = 6
    elif detailsselect == "4":
        ind = 7
    elif detailsselect == "5":
        ind = 8
    elif detailsselect == "6":
        ind = 9
    elif detailsselect == "7":
        ind = 10
    newdetails = input("Please enter your new details : ")
    allrec[ina][ind] = newdetails
    with open("userpass.txt", "w") as fh:
        nor = len(allrec)
        for cnt in range(0, nor):
            rec = ":".join(allrec[cnt])+"\n"
            fh.write(rec)
    
def gentransacid(turninline):
    with open("transactionid.txt","r") as tsfh:
        rec = tsfh.readline()
        reclist = rec.strip().split(":")
        if turninline == "transaction":
            pref = "TSC"
            oldid = reclist[0][3:]
        else:
            pass
    nextid = int(oldid) + 1
    if len(str(nextid)) == 1:
        newid = "0000"+str(nextid)
    elif len(str(nextid)) == 2:
        newid = "000"+str(nextid)
    elif len(str(nextid)) == 3:
        newid = "00"+str(nextid)
    elif len(str(nextid)) == 4:
        newid = "0"+str(nextid)
    elif len(str(nextid)) == 5:
        newid = str(nextid)
    newid = pref+newid
    if turninline == "transaction":
        reclist[0] = newid
    else:
        pass
    rec = ":".join(reclist)
    with open("transactionid.txt","w") as fh:
        fh.write(rec)
    return newid
    
def accountinfo(logdetails):
    with open("userpass.txt","r") as fh:
        print("="*190)
        print("User ID".center(10)+"|"+"User Password".center(14)+"|"+"User Name".center(15)+"|"+"Account Type".center(14)+"|"+"Account Model".center(15)+"|"+"Account Balance".center(17)+"|"+"Phone Number".center(15)+"|"+"Date of Birth".center(16)+"|"+"Residential Address".center(50)+"|"+"Age".center(5)+"|"+"Occupation".center(14)+"|")
        print("="*190)
        print(logdetails[0].ljust(10)+"|"+logdetails[1].ljust(14)+"|"+logdetails[2].ljust(15)+"|"+logdetails[3].ljust(14)+"|"+logdetails[4].ljust(15)+"|"+logdetails[5].ljust(17)+"|"+logdetails[6].ljust(15)+"|"+logdetails[7].ljust(16)+"|"+logdetails[8].ljust(50)+"|"+logdetails[9].ljust(5)+"|"+logdetails[10].ljust(14)+"|")
    print("\n\n\n")

def withdrawdeposit(logdetails):
    transactionid = gentransacid("transaction")
    print("Transaction ID :",transactionid)
    print("Customer ID : ",logdetails[0])
    transactiontype = input("Please enter your transaction type [W/D] [Q if you want to return to menu] : ")
    if transactiontype == "Q":
        print("You have return to the menu!"+"\n")
        return
    elif transactiontype == "W":
        allrec = []
        with open("userpass.txt","r") as fh:
            for rec in fh:
                reclist = rec.strip().split(":")
                allrec.append(reclist)
        ind = -1
        nor = len(allrec)
        for cnt in range(0,nor):
            if logdetails[4] == allrec[cnt][4]:
                ind = cnt
                break
                    
        if logdetails[4] == "Savings":
            print("Your current balance is : "+logdetails[5])
            print("Your account model is Savings with the minimum of RM 100")
            withdraw = 0
            while True:
                try:
                    withdraw = float(input("Please enter how much you want to withdraw : "))
                    break
                except ValueError:
                    print("You have input wrong value!...")
                    print("Please enter a valid number!..."+"\n")
            checkamount = float(logdetails[5]) - withdraw
            while checkamount < 100:
                print("Sorry, the minimum of Savings account is RM 100")
                withdraw = float(input("Please enter how much you want to withdraw : "))
                checkamount = float(logdetails[5]) - withdraw
            else:
                newamount = checkamount
                print("Withdraw successful!")
        else:
            print("Your current balance is : "+logdetails[5])
            print("Your account model is Current with the minimum of RM 500")
            withdraw = 0
            while True:
                try:
                    withdraw = float(input("Please enter how much you want to withdraw : "))
                    break
                except ValueError:
                    print("You have input wrong value!...")
                    print("Please enter a valid number!..."+"\n")
            checkamount = float(logdetails[5]) - withdraw
            while checkamount < 500:
                print("Sorry, the minimum of Current account is RM 500")
                withdraw = float(input("Please enter how much you want to withdraw : "))
                checkamount = float(logdetails[5]) - withdraw
            else:
                newamount = checkamount
                print("Withdraw successful!")
        ind = -1
        nor = len(allrec)
        for cnt in range(0,nor):
            if logdetails[0] == allrec[cnt][0]:
                ind = cnt
                break
            
        allrec[ind][5] = str(newamount)
        with open("userpass.txt","w") as fh:
            nor = len(allrec)
            for cnt in range(0,nor):
                rec = ":".join(allrec[cnt])+"\n"
                fh.write(rec)
        print("Your current balance is : "+str(newamount)+"\n")
    elif transactiontype == "D":
        allrec = []
        with open("userpass.txt","r") as fh:
            for rec in fh:
                reclist = rec.strip().split(":")
                allrec.append(reclist)
        ind = -1
        nor = len(allrec)
        for cnt in range(0,nor):
                if logdetails[0] == allrec[cnt][0]:
                      ind = cnt
                      break    
        print("Your current balance is : "+allrec[cnt][5])
        while True:
            try:
                deposit = float(input("Please enter how much you want to deposit : "))
                break
            except ValueError:
                print("You have input wrong value!...")
                print("Please enter a valid number!..."+"\n")
        newamount = float(logdetails[5]) + deposit      
        ind = -1
        nor = len(allrec)
        for cnt in range(0,nor):
            if logdetails[0] == allrec[cnt][0]:
                ind = cnt
                break

        allrec[ind][5] = str(newamount)
        with open("userpass.txt","w") as fh:
            nor = len(allrec)
            for cnt in range(0,nor):
                rec = ":".join(allrec[cnt])+"\n"
                fh.write(rec)

        print("Deposit Successful!")
        print("Your current balance is : "+str(newamount)+"\n")
    else:
        print("You have entered neither the choises!"+"\n")
        return 
    date = datetime.date.today()
    with open("withdrawdeposit.txt","a") as thfh:
        rec = transactionid+":"+logdetails[0]+":"+transactiontype+":"+str(newamount)+":"+str(date)+"\n"
        thfh.write(rec)


def mutationstaffsu():
    with open("withdrawdeposit.txt","r") as fh:
        print("="*110)
        print("Transaction ID".ljust(15)+"|"+"User ID".ljust(14)+"|"+"Transaction Type".ljust(18)+"|"+"Acount Balance".ljust(14)+"|"+"Date".ljust(20))
        print("="*110)
        for rec in fh:
              reclist = rec.strip().split(":")
              print(reclist[0].ljust(15)+"|"+ reclist[1].ljust(14)+"|"+ reclist[2].center(18)+"|"+reclist[3].center(14)+"|"+reclist[4].ljust(20))
    print("\n\n\n")

def mutationcustomer(logdetails):
    with open("withdrawdeposit.txt","r") as fh:
        startdate = input("Enter start date [Year-Month-Day: 2021-09-18] [Q  to return to menu]: ")
        enddate = input("Enter end date [Year-Month-Day: 2021-09-18] [Press any to return] : ")
        valid_date = True
        if startdate == "Q" or enddate == "Q":
            print("You have return to the menu!"+"\n")
            return
        try:
            startdate_date = datetime.datetime.strptime(startdate, "%Y-%m-%d")
            enddate_date = datetime.datetime.strptime(enddate, "%Y-%m-%d")
        except ValueError:
            valid_date = False
        while valid_date == False:
            print("Error in date given!!! Invalid date!!!")
            startdate = input("Enter start date [Year-Month-Day: 2021-09-18] : ")
            enddate = input("Enter end date [Year-Month-Day: 2021-09-18] : ")
            valid_date = True
            try:
                startdate_date = datetime.datetime.strptime(startdate, "%Y-%m-%d")
                enddate_date = datetime.datetime.strptime(enddate, "%Y-%m-%d")
            except ValueError:
                valid_date = False
        cusid = logdetails[0]
        print("="*90)
        print("Transaction ID".ljust(15)+"|"+"Customer ID".ljust(14)+"|"+"Transaction Type".ljust(30)+"|"+"Account Balance".ljust(17)+"|"+"Date".ljust(20))
        print("="*90) 
        for rec in fh:
            reclist = rec.strip().split(":")
            comp_str = reclist[4]
            comp_date = datetime.datetime.strptime(comp_str, "%Y-%m-%d")
            userid = reclist[1]
            if comp_date >= startdate_date and comp_date <= enddate_date and cusid == userid:
                print(reclist[0].ljust(15)+"|"+reclist[1].ljust(14)+"|"+reclist[2].ljust(30)+"|"+reclist[3].ljust(17)+"|"+reclist[4].ljust(20)) 
    print("\n\n\n")       
            
            
def superusermenu():
    while True:
        print("SUPER USER MENU")
        print("===============")
        print("\n\t1. Add new admin staff account")
        print("\t2. Display All user accounts")
        print("\t3. Mutation of All Customers")
        print("\t4. LOGOUT from the system")
        ans = input("Please enter your choice : ")
        if ans == "1":
            addstaff()
        elif ans == "2":
            dispalluser()
        elif ans == "3":
            mutationstaffsu()
        elif ans == "4":
              break
            
def adminstaffmenu(logdetails):
    while True:
        print("ADMIN STAFF MENU for: ",logdetails[2])
        print("================================")
        print("\n\t1. Register a new Customer")
        print("\t2. Display All user accounts")
        print("\t3. Mutation of All Customers")
        print("\t4. Modify Customer's Details")
        print("\t5. Change Password")
        print("\t6. LOGOUT from the system")
        ans = input("Please enter your choice : ")
        if ans == "1":
              addcustomer(logdetails)
        elif ans == "2":
              dispalluser()
        elif ans == "3":
              mutationstaffsu()
        elif ans == "4":
              modifydetails()
        elif ans == "5":
              changepass(logdetails)
        elif ans == "6":
              break

def customermenu(logdetails):
    while True:
        print("CUSTOMER MENU for : ",logdetails[2])
        print("===============")
        print("\n\t1. Show Account Information and Balance")
        print("\t2. Deposit and Withdraw money")
        print("\t3. Transaction History")
        print("\t4. Change Password")
        print("\t5. LOGOUT from the system")
        ans = input("Please enter your choice : ")
        if ans == "1":
              accountinfo(logdetails)
        elif ans == "2":
              withdrawdeposit(logdetails)
              break
        elif ans == "3":
              mutationcustomer(logdetails)
        elif ans == "4":
              changepass(logdetails)
        elif ans == "5":
              break

### MAIN LOGIC
#=============
while True:
      loginstat = userlogin()
      if loginstat != "notfound":
            print("Welcome to the System "+loginstat[2])
            if loginstat[3] == "1":
                  superusermenu()
            elif loginstat [3] == "2":
                  adminstaffmenu(loginstat)
            elif loginstat [3] == "3":
                  customermenu(loginstat)
      else:
            print("INVALID LOGIN CREDENTIALS...!!!!")
      ans = input("Press Q to Quit the SYSTEM.. Another Key to Continue....")
      if ans == "Q":
            break
