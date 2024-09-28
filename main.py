from datetime import datetime
import ast

ans = 'y'
mfile = 'master.txt'
tfile = 'transaction.txt'
dt = datetime.now()
tdate = str(dt.day) + "-" + str(dt.month) + "-" + str(dt.year)

while ans.lower() == 'y':
    print("1. Open Account")
    print("2. Deposit")
    print("3. Withdraw Account")
    print("4. Show balance")
    print("5. Exit")
    
    ch = int(input("Enter the key: "))
    
    if ch == 1:
        with open(mfile, "a+") as file:
            name = input("Name: ")
            accountno = int(input("Account no: "))
            amount = float(input("Amount: "))
            mlist = [name,accountno, tdate, amount]
            file.write(str(mlist) + "\n")
            print("Thanks for opening the account.")
    
    elif ch == 2:
        with open(mfile, 'r') as file:
            alldata = file.readlines()
        
        accountno = int(input("Account no: "))
        amount = float(input("Amount to deposit: "))
        
        for index, data in enumerate(alldata):
            xdata = ast.literal_eval(data)
            if accountno == xdata[1]:
                xdata[3] += amount
                alldata[index] = str(xdata) + '\n'
                
                with open(mfile, 'w') as nfile:
                    nfile.writelines(alldata)
                
                tdata = [accountno, tdate, 'D', amount]
                with open(tfile, 'a+') as hfile:
                    hfile.write(str(tdata) + "\n")
                
                print("Deposit successful.")
                break
        else:
            print("Account not found.")
    
    elif ch == 3:
        with open(mfile, 'r') as file:
            alldata = file.readlines()
        
        accountno = int(input("Account no: "))
        amount = float(input("Amount to withdraw: "))
        for index, data in enumerate(alldata):
            xdata = ast.literal_eval(data)
            if accountno == xdata[1]:
                if xdata[3] >= amount:
                    xdata[3] -= amount
                    alldata[index] = str(xdata) + '\n'
                    
                    with open(mfile, 'w') as nfile:
                        nfile.writelines(alldata)
                    
                    tdata = [name,accountno, tdate, 'W', amount]
                    with open(tfile, 'a+') as hfile:
                        hfile.write(str(tdata) + "\n")
                    
                    print("Withdrawal successful.")
                else:
                    print("Insufficient funds.")
                break
        else:
            print("Account not found.")
    
    elif ch == 4:
        with open(mfile, 'r') as rfile:
            alldata = rfile.readlines()
        
        accountno = int(input("Account no: "))
        
        for xdata in alldata:
            data = ast.literal_eval(xdata)
            if data[1] == accountno:
                print(f"Balance for account {accountno}: {data[3]}")
                break
        else:
            print("Account not found.")
    
    elif ch == 5:
        break
    
    print("Are you still in the bank (y/n)?")
    ans = input()

print("Thank you for using our bank service!")