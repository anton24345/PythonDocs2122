#Antono
#EzBank 1
import basics

app = basics.newProgram()

user = basics.newUser()

app.balance = 1000

while app.running:
    print("Your balance is " + str(app.balance))
    
    user.choice = input("Do you want to deposit 1, withdraw 2, or end 3")
    
    if user.choice == "1":
        
        user.deposit = input(" How much will you like to deposit")

        user.deposit=int(user.deposit)
        app.balance=app.balance+user.deposit
        
        
    elif user.choice == "2":
        user.withdraw = input("How much will you like to withdraw")
        user.withdraw=int(user.withdraw)
        if user.withdraw>app.balance:
            print("You don't have enough money")
        else:
            app.balance=app.balance-user.withdraw
            

    elif user.choice == "3":
        app.running = False
        print("END")
    else:
        print("Your choice was invalid")

    
 
    
        
    



        

        

    

        

        

        

        

        

        

        

        
