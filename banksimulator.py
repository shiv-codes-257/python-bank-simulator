balance = 0
while True:
    choice = input("hello welcome to the banking app, how can I assist you today? ")
    if choice == "create an account":
        name = input("enter your name: ")
        initial_balance = balance
        print("your account has been created! name: " , name + " your balance is ", initial_balance )
    elif choice == "deposit":
        deposit = int(input("how much money do you want to deposit? "))
        if deposit <=0 :
            print("deposit invalid")
        else:
            balance = balance + deposit
            print("your bank balance is" , balance)
    elif choice == "withdraw":
        withdraw = int(input("how much money do you want to withdraw? "))
        balance = balance - withdraw
        print("withdrawal succesful, your bank balance is now", balance)
        if withdraw <= 0:
            print("invalid withdrawal amount")
        elif withdraw > balance:
            print("withdrawal amount greater than balance")
    elif choice == "quit":
        break
    else:
        print("invalid option")
